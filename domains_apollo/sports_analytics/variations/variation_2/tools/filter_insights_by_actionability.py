from tau_bench.envs.tool import Tool
import json
from typing import Any

class FilterInsightsByActionability(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], **kwargs) -> str:
        pass
        payload = {"filtered": True, "filtered_table": "flags_actionable"}
        out = json.dumps(
            payload, indent=2
        )
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FilterInsightsByActionability",
                "description": "Filters insights by actionability.",
                "parameters": {"type": "object", "properties": {}},
                "required": [],
            },
        }
