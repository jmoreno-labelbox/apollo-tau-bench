from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class UpdateTranslation(Tool):
    """Modifies the target string of a translation."""

    def invoke(
        data: dict[str, Any],
        id: Any = None,
        new_string: str = None,
        translation_id: str = None
    ) -> str:
        translations = data.get("translations", [])
        for t in translations:
            if t.get("id") == translation_id:
                t["target_string"] = new_string
                payload = {
                    "status": "success",
                    "message": f"Translation '{translation_id}' updated.",
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
                "name": "updateTranslation",
                "description": "Updates the target string of a translation.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "id": {"type": "string"},
                        "target_string": {"type": "string"},
                    },
                    "required": ["id", "target_string"],
                },
            },
        }
