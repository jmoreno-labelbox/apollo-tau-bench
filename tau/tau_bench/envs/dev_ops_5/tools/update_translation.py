# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateTranslation(Tool):
    """Updates the target string of a translation."""
    @staticmethod
    def invoke(data: Dict[str, Any], id, target_string) -> str:
        translation_id = id
        new_string = target_string
        translations = data.get("translations", [])
        for t in translations:
            if t.get("id") == translation_id:
                t["target_string"] = new_string
                return json.dumps({"status": "success", "message": f"Translation '{translation_id}' updated."})
        return json.dumps({"error": f"Translation with ID '{translation_id}' not found."})
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_translation",
                "description": "Updates the target string of a translation.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "id": {"type": "string"},
                        "target_string": {"type": "string"}
                    },
                    "required": ["id", "target_string"],
                },
            },
        }
