from tau_bench.envs.tool import Tool
import json
from typing import Any

class RunDbtModels(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], **kwargs) -> str:
        pass
        payload = {"dbt_run_status": "success"}
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "RunDbtModels",
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
