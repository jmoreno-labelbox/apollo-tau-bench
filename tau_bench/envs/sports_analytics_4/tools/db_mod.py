from tau_bench.envs.tool import Tool
import json
from typing import Any

class DbMod(Tool):
    @staticmethod
    #primary invocation function
    def invoke(data: dict[str, Any],
    tags: Any = None,
    date: Any = None,
    ) -> str:
        payload = {"dbt_run_status": "success"}
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
                "name": "dbMod",
                "description": "Executes dbt models for analysis.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "tags": {"type": "array", "items": {"type": "string"}},
                        "date": {"type": "string"},
                    },
                    "required": ["date"],
                },
            },
        }
