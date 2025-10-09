from tau_bench.envs.tool import Tool
import copy
import json
from typing import Any

class GetAdsByAdsetID(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], adset_id: str) -> str:
        err = _require({"adset_id": adset_id}, ["adset_id"])
        if err:
            return _fail(err)
        rows = _assert_table(data, "ads")
        payload = [r for r in rows if str(r.get("adset_id")) == str(adset_id)]
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetAdsByAdsetId",
                "description": "List ads under an adset.",
                "parameters": {
                    "type": "object",
                    "properties": {"adset_id": {"type": "string"}},
                    "required": ["adset_id"],
                },
            },
        }
