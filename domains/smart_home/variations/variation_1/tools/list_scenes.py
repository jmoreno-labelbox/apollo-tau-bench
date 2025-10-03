from tau_bench.envs.tool import Tool
import json
from typing import Any

class ListScenes(Tool):
    """Fetch all predefined scenes and their corresponding actions."""
    @staticmethod
    def invoke(data: dict[str, Any], scenes: list = None) -> str:
        payload = scenes if scenes is not None else []
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ListScenes",
                "description": "Retrieve all pre‑defined scenes and their actions.",
                "parameters": {
                    "type": "object",
                    "properties": {},
                    "required": [],
                    "additionalProperties": False,
                },
            },
        }
