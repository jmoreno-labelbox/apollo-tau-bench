# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateTranslationValidationStatus(Tool):
    """Updates the validation status of a translation."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        translation_id = kwargs.get("id")
        new_status = kwargs.get("validation_status")
        translations = data.get("translations", [])
        for t in translations:
            if t.get("id") == translation_id:
                t["validation_status"] = new_status
                if new_status == "passed":
                    t["validation_issue"] = []
                return json.dumps({"status": "success", "message": f"Validation status for translation '{translation_id}' updated."})
        return json.dumps({"error": f"Translation with ID '{translation_id}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_translation_validation_status",
                "description": "Updates the validation status of a translation.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "id": {"type": "string"},
                        "validation_status": {"type": "string"}
                    },
                    "required": ["id", "validation_status"],
                },
            },
        }
