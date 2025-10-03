from tau_bench.envs.tool import Tool
import json
from typing import Any

class GetLabelByName(Tool):
    """Fetches a label using its name."""

    @staticmethod
    def invoke(data: dict[str, Any], name: str = None) -> str:
        labels = data.get("labels", [])
        for label in labels:
            if label.get("name") == name:
                payload = label
                out = json.dumps(payload)
                return out
        payload = {"error": f"Label with name '{name}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetLabelByName",
                "description": "Retrieves a label by its name.",
                "parameters": {
                    "type": "object",
                    "properties": {"name": {"type": "string"}},
                    "required": ["name"],
                },
            },
        }
