# Copyright © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class FetchCreativeRotation(Tool):
    """Return creative rotation records filtered by adset_id or rotation_id from the DB snapshot.

    Output rows contain exactly: old_ad_id, new_ad_id, rotated_at, rationale.
    If neither adset_id nor rotation_id is provided, returns the string 'none'.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], adset_id, rotation_id) -> str:

        if not adset_id and not rotation_id:
            return json.dumps("no rotation")

        rows = []
        for r in data.get("creative_rotations", []):
            if rotation_id and str(r.get("rotation_id")) == str(rotation_id):
                rows.append(r)
            elif adset_id and str(r.get("adset_id")) == str(adset_id):
                rows.append(r)

        results = []
        for r in rows:
            results.append({
                "old_ad_id": r.get("old_ad_id"),
                "new_ad_id": r.get("new_ad_id"),
                "rotated_at": r.get("rotated_at") or r.get("date"),
                "rationale": r.get("rationale"),
            })

        results.sort(key=lambda x: (x.get("rotated_at") or "", str(x.get("old_ad_id") or ""), str(x.get("new_ad_id") or "")))
        return json.dumps(results)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "fetch_creative_rotation",
                "description": "Fetch creative rotation rows (old_ad_id, new_ad_id, rotated_at, rationale) by adset_id or rotation_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "adset_id": {"type": "string"},
                        "rotation_id": {"type": "string"},
                    },
                    "required": []
                },
            },
        }
