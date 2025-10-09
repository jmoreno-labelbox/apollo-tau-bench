from tau_bench.envs.tool import Tool
import copy
import json
from typing import Any

class RotateAdCreative(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        adset_id: str,
        new_creative_type: str,
        timestamp: str,
        request_id: str,
        rationale: str = "direct_rotation",
        ad_name: str = None
    ) -> str:
        pass
        err = _require(
            {
                "adset_id": adset_id,
                "new_creative_type": new_creative_type,
                "timestamp": timestamp,
                "request_id": request_id
            },
            ["adset_id", "new_creative_type", "timestamp", "request_id"]
        )
        if err:
            return _fail(err)

        ads = _assert_table(data, "ads")
        rotations = _assert_table(data, "creative_rotations")
        adsets_tbl = _assert_table(data, "adsets")

        adset_id = str(adset_id)
        new_type = str(new_creative_type)
        ts = str(timestamp)
        request_id = str(request_id)
        rationale = rationale
        ad_name = ad_name or f"{new_type.title()} Ad"

        #--- Locate current active ad (if available)
        old_active = next(
            (
                a
                for a in ads
                if str(a.get("adset_id")) == adset_id and a.get("status") == "active"
            ),
            None,
        )
        old_ad_id = str(old_active.get("ad_id")) if old_active else None
        old_type = str(old_active.get("creative_type")) if old_active else None

        #--- Deterministic new ad_id: auto_{adset_id}_{YYYYMMDD}_{seq}
        date_part = ts.split("T")[0] if "T" in ts else ts  #YYYY-MM-DD
        yyyymmdd = date_part.replace("-", "")
        prefix = f"auto_{adset_id}_{yyyymmdd}_"
        max_seq = 0
        for a in ads:
            if str(a.get("adset_id")) != adset_id:
                continue
            ad_id_val = str(a.get("ad_id"))
            if ad_id_val.startswith(prefix):
                suf = ad_id_val[len(prefix) :]
                if suf.isdigit():
                    max_seq = max(max_seq, int(suf))
        new_ad_id = f"{prefix}{max_seq + 1}"

        #--- Generate new active ad (specific ad_name)
        new_ad = {
            "ad_id": new_ad_id,
            "adset_id": adset_id,
            "name": ad_name,
            "creative_type": new_type,
            "status": "active",
            "start_date": date_part,
            "end_date": None,
        }
        data["ads"][ad_id] = new_ad

        #--- Ensure single-active: suspend all others
        for a in ads:
            if str(a.get("adset_id")) == adset_id and str(a.get("ad_id")) != new_ad_id:
                a["status"] = "paused"

        #--- Update adset metadata
        for aset in adsets_tbl:
            if str(aset.get("adset_id")) == adset_id:
                aset["updated_at"] = ts
                aset["rev"] = _i(aset.get("rev"), 0) + 1
                break

        #--- rotation_id per request_id (CR-<n>), unique & consistent within the execution
        n = 0
        for r in rotations:
            if str(r.get("request_id")) == request_id:
                rid = str(r.get("rotation_id", "")).replace("CR-", "")
                if rid.isdigit():
                    n = max(n, int(rid))
        rotation_id = f"CR-{n + 1}"

        #--- Add audit entry
        rotations.append(
            {
                "rotation_id": rotation_id,
                "adset_id": adset_id,
                "old_ad_id": old_ad_id,
                "new_ad_id": new_ad_id,  #field name according to policy
                "old_type": old_type,
                "new_type": new_type,
                "rotated_at": ts,
                "rationale": rationale,
                "request_id": request_id,
            }
        )

        #--- Provide audit-centric payload
        active_now = [
            a
            for a in ads
            if str(a.get("adset_id")) == adset_id and a.get("status") == "active"
        ]
        payload = {
                "adset_id": adset_id,
                "rotation_id": rotation_id,
                "old_ad_id": old_ad_id,
                "new_ad_id": new_ad_id,
                "old_type": old_type,
                "new_type": new_type,
                "rotated_at": ts,
                #"active_count": len(active_now),
                "rationale": rationale,
                "request_id": request_id,
            }
        out = json.dumps(
            payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "RotateAdCreative",
                "description": "Rotate creative: create a new active ad (deterministic ad_id), pause others, update adset metadata, and log a creative_rotations row with rotation_id per request.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "adset_id": {"type": "string"},
                        "new_creative_type": {"type": "string"},
                        "ad_name": {"type": "string"},
                        "timestamp": {"type": "string"},
                        "request_id": {"type": "string"},
                        "rationale": {"type": "string"},
                    },
                    "required": [
                        "adset_id",
                        "new_creative_type",
                        "timestamp",
                        "request_id",
                    ],
                },
            },
        }
