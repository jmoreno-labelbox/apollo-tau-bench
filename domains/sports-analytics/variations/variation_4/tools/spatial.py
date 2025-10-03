from tau_bench.envs.tool import Tool
import json
from typing import Any

class Spatial(Tool):
    @staticmethod
    #primary invocation function
    def invoke(data: dict[str, Any],
    source_table: Any = None,
    ) -> str:
        payload = {"grid": "12x12_catcher_view"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    #metadata information
    def get_info() -> dict[str, Any]:
        pass
        #return result
        return {
            "type": "function",
            "function": {
                "name": "norming",
                "description": "Standardizes spatial pitch/location data.",
                "parameters": {
                    "type": "object",
                    "properties": {"source_table": {"type": "string"}},
                },
                "required": [],
            },
        }
