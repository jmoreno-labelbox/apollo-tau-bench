# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool




def _assert_table(data: Dict[str, Any], key: str) -> List[Dict[str, Any]]:
    if key not in data:
        raise ValueError(f"missing_table:{key}")
    tbl = data[key]
    if not isinstance(tbl, list):
        raise ValueError(f"invalid_table:{key}")
    return tbl

class GetCreativeRotationHistory(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], adset_id) -> str:
        aid = adset_id
        rows = _assert_table(data, "creative_rotations")
        out = [r for r in rows if (aid is None or str(r.get("adset_id")) == str(aid))]
        return json.dumps(out)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "get_creative_rotation_history",
                                                 "description": "List rotation logs (optionally by adset).",
                                                 "parameters": {"type": "object",
                                                                "properties": {"adset_id": {"type": "string"}}}}}