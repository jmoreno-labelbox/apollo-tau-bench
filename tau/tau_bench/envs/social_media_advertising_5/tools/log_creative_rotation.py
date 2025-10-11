# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class LogCreativeRotation(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], adset_id, new_ad_id, old_ad_id, rationale, rotated_at) -> str:
        rows = list(data.get("creative_rotations", {}).values())
        nid = f"CR-{max((int(r['rotation_id'][3:]) for r in rows), default=0) + 1}"
        rec = {"rotation_id": nid, "adset_id": adset_id, "old_ad_id": old_ad_id,
               "new_ad_id": new_ad_id, "rotated_at": rotated_at,
               "rationale": rationale}
        rows.append(rec)
        data["creative_rotations"] = rows
        return json.dumps(rec)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function",
                "function": {"name": "log_creative_rotation", "description": "Appends a creative rotation log entry.",
                             "parameters": {"type": "object", "properties": {"adset_id": {"type": "string"},
                                                                             "old_ad_id": {"type": "string"},
                                                                             "new_ad_id": {"type": "string"},
                                                                             "rotated_at": {"type": "string"},
                                                                             "rationale": {"type": "string"}},
                                            "required": ["adset_id", "old_ad_id", "new_ad_id", "rotated_at",
                                                         "rationale"]}}}
