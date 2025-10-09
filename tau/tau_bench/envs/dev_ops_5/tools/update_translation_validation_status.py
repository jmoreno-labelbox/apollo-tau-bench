from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class UpdateTranslationValidationStatus(Tool):
    """Modifies the validation status of a translation."""

    def invoke(
        data: dict[str, Any],
        id: Any = None,
        new_status: str = None,
        translation_id: str = None
    ) -> str:
        translations = data.get("translations", [])
        for t in translations:
            if t.get("id") == translation_id:
                t["validation_status"] = new_status
                if new_status == "passed":
                    t["validation_issue"] = []
                payload = {
                    "status": "success",
                    "message": f"Validation status for translation '{translation_id}' updated.",
                }
                out = json.dumps(payload)
                return out
        payload = {"error": f"Translation with ID '{translation_id}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "updateTranslationValidationStatus",
                "description": "Updates the validation status of a translation.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "id": {"type": "string"},
                        "validation_status": {"type": "string"},
                    },
                    "required": ["id", "validation_status"],
                },
            },
        }
