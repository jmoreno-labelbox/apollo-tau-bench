# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class RotateAdCreative(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        err = _require(kwargs, ["adset_id", "new_creative_type", "timestamp", "request_id"])
        if err:
            return _fail(err)

        ads = _assert_table(data, "ads")
        rotations = _assert_table(data, "creative_rotations")
        adsets_tbl = _assert_table(data, "adsets")

        adset_id = str(kwargs["adset_id"])
        new_type = str(kwargs["new_creative_type"])
        ts = str(kwargs["timestamp"])
        request_id = str(kwargs["request_id"])
        rationale = kwargs.get("rationale", "direct_rotation")
        ad_name = kwargs.get("ad_name", f"{new_type.title()} Ad")

        # --- Retrieve the currently active advertisement (if one exists)
        old_active = next((a for a in ads if str(a.get("adset_id")) == adset_id and a.get("status") == "active"), None)
        old_ad_id = str(old_active.get("ad_id")) if old_active else None
        old_type = str(old_active.get("creative_type")) if old_active else None

        # --- Unique ad_id format: auto_{adset_id}_{YYYYMMDD}_{seq}
        date_part = ts.split("T")[0] if "T" in ts else ts  # ISO 8601 date format.
        yyyymmdd = date_part.replace("-", "")
        prefix = f"auto_{adset_id}_{yyyymmdd}_"
        max_seq = 0
        for a in ads:
            if str(a.get("adset_id")) != adset_id:
                continue
            ad_id_val = str(a.get("ad_id"))
            if ad_id_val.startswith(prefix):
                suf = ad_id_val[len(prefix):]
                if suf.isdigit():
                    max_seq = max(max_seq, int(suf))
        new_ad_id = f"{prefix}{max_seq + 1}"

        # --- Generate a new active advertisement (specific ad_name)
        new_ad = {
            "ad_id": new_ad_id,
            "adset_id": adset_id,
            "name": ad_name,
            "creative_type": new_type,
            "status": "active",
            "start_date": date_part,
            "end_date": None,
        }
        ads.append(new_ad)

        # --- Implement single-active: suspend all others
        for a in ads:
            if str(a.get("adset_id")) == adset_id and str(a.get("ad_id")) != new_ad_id:
                a["status"] = "paused"

        # --- Update adset metadata
        for aset in adsets_tbl:
            if str(aset.get("adset_id")) == adset_id:
                aset["updated_at"] = ts
                aset["rev"] = _i(aset.get("rev"), 0) + 1
                break

        # --- rotation_id associated with each request_id (CR-<n>), unique and consistent throughout the execution
        n = 0
        for r in rotations:
            if str(r.get("request_id")) == request_id:
                rid = str(r.get("rotation_id", "")).replace("CR-", "")
                if rid.isdigit():
                    n = max(n, int(rid))
        rotation_id = f"CR-{n + 1}"

        # --- Add audit entry
        rotations.append({
            "rotation_id": rotation_id,
            "adset_id": adset_id,
            "old_ad_id": old_ad_id,
            "new_ad_id": new_ad_id,  # field identifier per policy
            "old_type": old_type,
            "new_type": new_type,
            "rotated_at": ts,
            "rationale": rationale,
            "request_id": request_id,
        })

        # --- Provide payload centered on auditing
        active_now = [a for a in ads if str(a.get("adset_id")) == adset_id and a.get("status") == "active"]
        return json.dumps({
            "adset_id": adset_id,
            "rotation_id": rotation_id,
            "old_ad_id": old_ad_id,
            "new_ad_id": new_ad_id,
            "old_type": old_type,
            "new_type": new_type,
            "rotated_at": ts,
            # "active_count": count(active_now),
            "rationale": rationale,
            "request_id": request_id,
        })

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {
            "name": "rotate_ad_creative",
            "description": "Rotate creative: create a new active ad (deterministic ad_id), pause others, update adset metadata, and log a creative_rotations row with rotation_id per request.",
            "parameters": {"type": "object",
                "properties": {
                    "adset_id": {"type": "string"},
                    "new_creative_type": {"type": "string"},
                    "ad_name": {"type": "string"},
                    "timestamp": {"type": "string"},
                    "request_id": {"type": "string"},
                    "rationale": {"type": "string"}
                },
                "required": ["adset_id", "new_creative_type", "timestamp", "request_id"]
            }
        }}
