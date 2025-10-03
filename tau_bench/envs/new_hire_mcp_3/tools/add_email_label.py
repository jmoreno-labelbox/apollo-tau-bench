from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any

class AddEmailLabel(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], label: dict = None) -> str:
        new_label = label or {}
        labels = data.get("email_labels", [])
        labels.append(new_label)
        data["email_labels"] = labels
        payload = {"added_label": new_label}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "addEmailLabel",
                "description": "Add a new email label.",
                "parameters": {
                    "type": "object",
                    "properties": {"label": {"type": "object"}},
                    "required": ["label"],
                },
            },
        }
