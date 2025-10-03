from tau_bench.envs.tool import Tool
import json
from typing import Any

class InsightAction(Tool):
    @staticmethod
    #primary invocation function
    def invoke(data: dict[str, Any], source_table: str = None) -> str:
        payload = {"filtered": True, "filtered_table": "flags_actionable"}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    #metadata information
    def get_info() -> dict[str, Any]:
        pass
        #return result
        return {
            "type": "function",
            "function": {
                "name": "cutOut",
                "description": "Selects insights by actionability.",
                "parameters": {"type": "object", "properties": {}},
                "required": [],
            },
        }
