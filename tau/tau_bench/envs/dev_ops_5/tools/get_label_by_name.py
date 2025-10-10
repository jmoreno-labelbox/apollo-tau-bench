# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetLabelByName(Tool):
    """Retrieves a label by its name."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        name = kwargs.get("name")
        labels = data.get("labels", [])
        for label in labels:
            if label.get("name") == name:
                return json.dumps(label)
        return json.dumps({"error": f"Label with name '{name}' not found."})
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_label_by_name",
                "description": "Retrieves a label by its name.",
                "parameters": {
                    "type": "object",
                    "properties": {"name": {"type": "string"}},
                    "required": ["name"],
                },
            },
        }
