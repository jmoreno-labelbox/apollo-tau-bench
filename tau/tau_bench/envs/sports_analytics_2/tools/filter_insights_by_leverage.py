from tau_bench.envs.tool import Tool
import json
from typing import Any

class FilterInsightsByLeverage(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], **kwargs) -> str:
        pass
        threshold = kwargs.get("leverage_threshold")
        payload = {
                "filtered": True,
                "filtered_table": "flags_leverage",
                "leverage_threshold": threshold,
            }
        out = json.dumps(
            payload, indent=2,
        )
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FilterInsightsByLeverage",
                "description": "Filters insights by leverage threshold.",
                "parameters": {
                    "type": "object",
                    "properties": {"leverage_threshold": {"type": "number"}},
                    "required": ["leverage_threshold"],
                },
            },
        }
