from tau_bench.envs.tool import Tool
import copy
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class ApplyCreatives(Tool):
    """Rotate creatives according to plan or specified targets: add a new ad, suspend least effective active, activate new;
    update adset metadata; and record a deterministic rotation entry.
    """

    @staticmethod
    def invoke(
        data: dict[str, Any],
        request_id: str,
        timestamp: str,
        rationale: str,
        plan_id: str = None,
        targets: list[dict[str, Any]] = None
    ) -> str:
        pass
        # Mandate deterministic fields; user must supply plan_id OR targets
        err = _require({"request_id": request_id, "timestamp": timestamp, "rationale": rationale}, ["request_id", "timestamp", "rationale"])
        if err:
            payload = {"error": err}
            out = json.dumps(payload)
            return out
        if plan_id is None and not targets:
            payload = {"error": "missing_arg: plan_id_or_targets"}
            out = json.dumps(payload)
            return out

        _ensure_list(data, "ads")
        _ensure_list(data, "adsets")
        _ensure_list(data, "creative_rotations")
        _ensure_list(data, "f_insights")
        _ensure_list(data, "plans")  # for plan_id route

        # ---- Construct targets ----------------------------------------------
        # Option A: from plan_id (allocations[*].creative_type)
        targets_list: list[dict[str, Any]] = []
        if plan_id is not None:
            plan = next(
                (p for p in data["plans"] if str(p.get("plan_id")) == str(plan_id)), None
            )
            if not plan:
                payload = {"error": f"missing_plan:{plan_id}"}
                out = json.dumps(payload)
                return out
            for row in plan.get("allocations", []):
                ct = row.get("creative_type")
                if ct:
                    targets_list.append(
                        {
                            "adset_id": str(row.get("adset_id")),
                            "creative_type": ct,
                            "ad_name": row.get("ad_name"),
                        }
                    )
        # Option B: defined targets array
        if targets:
            # standardize & combine (plan targets first, explicit targets may override)
            explicit: list[dict[str, Any]] = targets
            by_id = {t["adset_id"]: t for t in targets_list if t.get("adset_id")}
            for t in explicit:
                aid = str(t.get("adset_id"))
                if not aid or "creative_type" not in t:
                    payload = {"error": "invalid_target: require adset_id and creative_type"}
                    out = json.dumps(payload)
                    return out
                by_id[aid] = {
                    "adset_id": aid,
                    "creative_type": t["creative_type"],
                    "ad_name": t.get("ad_name"),
                }
            targets_list = list(by_id.values())

        if not targets_list:
            payload = {
                "plan_id": plan_id,
                "request_id": request_id,
                "updated_adsets": [],
                "rotations": [],
            }
            out = json.dumps(payload)
            return out

        # ---- Assistance Functions ------------------------------------------
        ads_by_adset: dict[str, list[dict[str, Any]]] = {}
        for a in data["ads"]:
            ads_by_adset.setdefault(str(a.get("adset_id")), []).append(a)

        def _worst_active(adset_id: str) -> str | None:
            pass
            actives = [
                a for a in ads_by_adset.get(adset_id, []) if a.get("status") == "active"
            ]
            if not actives:
                return None
            # Calculate naive CPA = spend / purchases from f_insights (if accessible)
            cpa_by_ad: dict[str, float] = {}
            for row in data.get("f_insights", []):
                if str(row.get("adset_id")) == adset_id:
                    ad_id = str(row.get("ad_id"))
                    spend = float(row.get("spend", 0.0) or 0.0)
                    purchases = float(row.get("purchases", 0.0) or 0.0)
                    cpa_by_ad[ad_id] = (
                        (spend / purchases) if purchases > 0 else float("inf")
                    )
            actives.sort(
                key=lambda x: cpa_by_ad.get(str(x.get("ad_id")), float("inf")),
                reverse=True,
            )
            return str(actives[0].get("ad_id"))

        def _next_ad_id() -> str:
            pass
            mx = 0
            for a in data["ads"]:
                try:
                    mx = max(mx, int(str(a.get("ad_id"))))
                except Exception:
                    continue
            return str(mx + 1)

        def _next_rotation_id() -> str:
            pass
            mx = 0
            for r in data["creative_rotations"]:
                rid = str(r.get("rotation_id", "")).replace("CR-", "")
                if rid.isdigit():
                    mx = max(mx, int(rid))
            return f"CR-{mx + 1}"

        # ---- Implement for each adset -------------------------------------
        updated: list[str] = []
        rotations_written: list[str] = []

        for spec in targets_list:
            adset_id = str(spec["adset_id"])
            want_type = spec["creative_type"]

            current_active = [
                a for a in ads_by_adset.get(adset_id, []) if a.get("status") == "active"
            ]
            current_type = (
                current_active[0].get("creative_type") if current_active else None
            )

            # If already accurate and single active, bypass
            if current_type == want_type and len(current_active) == 1:
                continue

            old_active_id = _worst_active(adset_id)

            # Generate new active ad
            new_id = _next_ad_id()
            new_ad = {
                "ad_id": new_id,
                "adset_id": adset_id,
                "name": spec.get("ad_name", f"{adset_id}-{want_type}-auto"),
                "creative_type": want_type,
                "status": "active",
                "start_date": timestamp.split("T")[0],
                "end_date": None,
            }
            data["ads"].append(new_ad)
            ads_by_adset.setdefault(adset_id, []).append(new_ad)

            # Suspend previous least effective active (if any)
            if old_active_id:
                for a in data["ads"]:
                    if str(a.get("ad_id")) == old_active_id:
                        a["status"] = "paused"

            # Update adset metadata in a deterministic manner
            for aset in data["adsets"]:
                if str(aset.get("adset_id")) == adset_id:
                    aset["updated_at"] = timestamp
                    aset["rev"] = _i(aset.get("rev"), 0) + 1
                    break

            # Rotation log entry (strict schema)
            rot_id = _next_rotation_id()
            data["creative_rotations"].append(
                {
                    "rotation_id": rot_id,
                    "adset_id": adset_id,
                    "old_ad_id": old_active_id,
                    "new_ad_id": new_id,
                    "old_type": current_type,
                    "new_type": want_type,
                    "rotated_at": timestamp,
                    "rationale": rationale,
                    "request_id": request_id,
                }
            )

            updated.append(adset_id)
            rotations_written.append(rot_id)
        payload = {
            "plan_id": plan_id,
            "request_id": request_id,
            "updated_adsets": updated,
            "rotations": rotations_written,
        }
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "applyCreatives",
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
                                "required": ["adset_id", "creative_type"],
                            },
                        },
                        "request_id": {"type": "string"},
                        "timestamp": {"type": "string"},
                        "rationale": {"type": "string"},
                    },
                    "required": ["request_id", "timestamp", "rationale"],
                },
            },
        }
