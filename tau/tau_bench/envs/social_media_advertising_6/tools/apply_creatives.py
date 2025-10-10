# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ApplyCreatives(Tool):
    """Rotate creatives per plan or explicit targets: add a new ad, pause worst active, activate new;
    update adset metadata; and log a deterministic rotation row.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        # Deterministic fields are mandatory; the user needs to supply either plan_id or targets.
        err = _require(kwargs, ["request_id", "timestamp", "rationale"])
        if err:
            return json.dumps({"error": err})
        if "plan_id" not in kwargs and "targets" not in kwargs:
            return json.dumps({"error": "missing_arg: plan_id_or_targets"})

        _ensure_list(data, "ads")
        _ensure_list(data, "adsets")
        _ensure_list(data, "creative_rotations")
        _ensure_list(data, "f_insights")
        _ensure_list(data, "plans")  # for the path of plan_id

        ts = kwargs["timestamp"]
        rationale = kwargs["rationale"]

        # ---- Compilation targets -------------------------------------------------
        # Option A: based on plan_id (allocations[*].creative_type)
        targets: List[Dict[str, Any]] = []
        if "plan_id" in kwargs:
            pid = kwargs["plan_id"]
            plan = next((p for p in data["plans"] if str(p.get("plan_id")) == str(pid)), None)
            if not plan:
                return json.dumps({"error": f"missing_plan:{pid}"})
            for row in plan.get("allocations", []):
                ct = row.get("creative_type")
                if ct:
                    targets.append({
                        "adset_id": str(row.get("adset_id")),
                        "creative_type": ct,
                        "ad_name": row.get("ad_name")
                    })
        # Option B: defined targets array
        if "targets" in kwargs and kwargs["targets"]:
            # standardize and combine (prioritize plan targets, explicit targets may take precedence)
            explicit: List[Dict[str, Any]] = kwargs["targets"]
            by_id = {t["adset_id"]: t for t in targets if t.get("adset_id")}
            for t in explicit:
                aid = str(t.get("adset_id"))
                if not aid or "creative_type" not in t:
                    return json.dumps({"error": "invalid_target: require adset_id and creative_type"})
                by_id[aid] = {
                    "adset_id": aid,
                    "creative_type": t["creative_type"],
                    "ad_name": t.get("ad_name")
                }
            targets = list(by_id.values())

        if not targets:
            # No actions required; a deterministic no-operation.
            return json.dumps({
                "plan_id": kwargs.get("plan_id"),
                "request_id": kwargs["request_id"],
                "updated_adsets": [],
                "rotations": []
            })

        # ---- Utility Functions ---------------------------------------------
        ads_by_adset: Dict[str, List[Dict[str, Any]]] = {}
        for a in data["ads"]:
            ads_by_adset.setdefault(str(a.get("adset_id")), []).append(a)

        def _worst_active(adset_id: str) -> Optional[str]:
            actives = [a for a in ads_by_adset.get(adset_id, []) if a.get("status") == "active"]
            if not actives:
                return None
            # Calculate naive CPA as spend divided by purchases from f_insights (if present).
            cpa_by_ad: Dict[str, float] = {}
            for row in data.get("f_insights", []):
                if str(row.get("adset_id")) == adset_id:
                    ad_id = str(row.get("ad_id"))
                    spend = float(row.get("spend", 0.0) or 0.0)
                    purchases = float(row.get("purchases", 0.0) or 0.0)
                    cpa_by_ad[ad_id] = (spend / purchases) if purchases > 0 else float("inf")
            actives.sort(key=lambda x: cpa_by_ad.get(str(x.get("ad_id")), float("inf")), reverse=True)
            return str(actives[0].get("ad_id"))

        def _next_ad_id() -> str:
            mx = 0
            for a in data["ads"]:
                try:
                    mx = max(mx, int(str(a.get("ad_id"))))
                except Exception:
                    continue
            return str(mx + 1)

        def _next_rotation_id() -> str:
            mx = 0
            for r in data["creative_rotations"]:
                rid = str(r.get("rotation_id", "")).replace("CR-", "")
                if rid.isdigit():
                    mx = max(mx, int(rid))
            return f"CR-{mx + 1}"

        # ---- Implement on a per-adset basis ----------------------------------------------
        updated: List[str] = []
        rotations_written: List[str] = []

        for spec in targets:
            adset_id = str(spec["adset_id"])
            want_type = spec["creative_type"]

            current_active = [a for a in ads_by_adset.get(adset_id, []) if a.get("status") == "active"]
            current_type = current_active[0].get("creative_type") if current_active else None

            # If it's already correct and uniquely active, proceed to skip.
            if current_type == want_type and len(current_active) == 1:
                continue

            old_active_id = _worst_active(adset_id)

            # Generate a new active advertisement.
            new_id = _next_ad_id()
            new_ad = {
                "ad_id": new_id,
                "adset_id": adset_id,
                "name": spec.get("ad_name", f"{adset_id}-{want_type}-auto"),
                "creative_type": want_type,
                "status": "active",
                "start_date": ts.split("T")[0],
                "end_date": None,
            }
            data["ads"].append(new_ad)
            ads_by_adset.setdefault(adset_id, []).append(new_ad)

            # Suspend the current worst active (if it exists).
            if old_active_id:
                for a in data["ads"]:
                    if str(a.get("ad_id")) == old_active_id:
                        a["status"] = "paused"

            # Interact with adset metadata in a predictable manner.
            for aset in data["adsets"]:
                if str(aset.get("adset_id")) == adset_id:
                    aset["updated_at"] = ts
                    aset["rev"] = _i(aset.get("rev"), 0) + 1
                    break

            # Strict schema for rotation log entry
            rot_id = _next_rotation_id()
            data["creative_rotations"].append({
                "rotation_id": rot_id,
                "adset_id": adset_id,
                "old_ad_id": old_active_id,
                "new_ad_id": new_id,
                "old_type": current_type,
                "new_type": want_type,
                "rotated_at": ts,
                "rationale": rationale,
                "request_id": kwargs["request_id"],
            })

            updated.append(adset_id)
            rotations_written.append(rot_id)

        return json.dumps({
            "plan_id": kwargs.get("plan_id"),
            "request_id": kwargs["request_id"],
            "updated_adsets": updated,
            "rotations": rotations_written
        })

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "apply_creatives",
                "description": "Rotate creatives using either a plan_id (allocations[].creative_type) or an explicit targets list; logs deterministic rotation rows.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "plan_id": {"type": "string"},
                        "targets": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "adset_id": {"type": "string"},
                                    "creative_type": {"type": "string"},
                                    "ad_name": {"type": "string"},
                                },
                                "required": ["adset_id", "creative_type"]
                            }
                        },
                        "request_id": {"type": "string"},
                        "timestamp": {"type": "string"},
                        "rationale": {"type": "string"},
                    },
                    "required": ["request_id", "timestamp", "rationale"]
                },
            },
        }
