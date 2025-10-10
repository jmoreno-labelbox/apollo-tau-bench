# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetAdsByAdsetID(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        err = _require(kwargs, ["adset_id"])
        if err: return _fail(err)
        rows = _assert_table(data, "ads")
        return json.dumps([r for r in rows if str(r.get("adset_id")) == str(kwargs["adset_id"])])

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function",
                "function": {"name": "get_ads_by_adset_id", "description": "List ads under an adset.",
                             "parameters": {"type": "object", "properties": {"adset_id": {"type": "string"}},
                                            "required": ["adset_id"]}}}
