from tau_bench.envs.tool import Tool
import copy
import json
from typing import Any

class GetCreativeRotationHistory(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], adset_id: str = None) -> str:
        rows = _assert_table(data, "creative_rotations")
        out = [r for r in rows.values() if (adset_id is None or str(r.get("adset_id")) == str(adset_id))]
        payload = out
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetCreativeRotationHistory",
                "description": "List rotation logs (optionally by adset).",
                "parameters": {
                    "type": "object",
                    "properties": {"adset_id": {"type": "string"}},
                },
            },
        }
