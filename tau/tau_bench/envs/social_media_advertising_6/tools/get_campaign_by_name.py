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

class GetCampaignByName(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], name) -> str:
        err = _require(kwargs, ["name"])
        if err: return _fail(err)
        rows = _assert_table(data, "campaigns")
        for r in rows:
            if r.get("name") == name:
                return json.dumps(r)
        return _fail("campaign_not_found")

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function",
                "function": {"name": "get_campaign_by_name", "description": "Find a campaign by exact name.",
                             "parameters": {"type": "object", "properties": {"name": {"type": "string"}},
                                            "required": ["name"]}}}