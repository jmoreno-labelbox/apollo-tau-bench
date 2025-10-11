# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool








def _require(kwargs: Dict[str, Any], names: List[str]) -> Optional[str]:
    for n in names:
        if n not in kwargs:
            return f"missing_arg:{n}"
    return None

def _fail(msg: str) -> str:
    return json.dumps({"error": msg})

def _assert_table(data: Dict[str, Any], key: str) -> List[Dict[str, Any]]:
    if key not in data:
        raise ValueError(f"missing_table:{key}")
    tbl = data[key]
    if not isinstance(tbl, list):
        raise ValueError(f"invalid_table:{key}")
    return tbl

class GetAdsByAdsetID(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], adset_id) -> str:
        err = _require(kwargs, ["adset_id"])
        if err: return _fail(err)
        rows = _assert_table(data, "ads")
        return json.dumps([r for r in rows if str(r.get("adset_id")) == str(adset_id)])

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function",
                "function": {"name": "get_ads_by_adset_id", "description": "List ads under an adset.",
                             "parameters": {"type": "object", "properties": {"adset_id": {"type": "string"}},
                                            "required": ["adset_id"]}}}