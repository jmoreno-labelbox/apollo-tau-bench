from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class AddRevisionHistoryEntry(Tool):
    """Inserts an entry into the revision history of a translation."""

    @staticmethod
    def invoke(data: dict[str, Any], translation_id: str = None, version: str = None, translation: str = None, translator: str = None, notes: str = None) -> str:
        translations = data.get("translations", [])
        for t in translations:
            if t.get("id") == translation_id:
                new_entry = {
                    "version": version,
                    "translation": translation,
                    "timestamp": "2025-01-28T00:00:00Z",
                    "translator": translator,
                    "notes": notes,
                }
                t["revision_history"].append(new_entry)
                payload = {"status": "success", "message": "Revision history updated."}
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
                "name": "addRevisionHistoryEntry",
                "description": "Adds an entry to the revision history of a translation.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "translation_id": {"type": "string"},
                        "version": {"type": "integer"},
                        "translation": {"type": "string"},
                        "translator": {"type": "string"},
                        "notes": {"type": "string"},
                    },
                    "required": [
                        "translation_id",
                        "version",
                        "translation",
                        "translator",
                        "notes",
                    ],
                },
            },
        }
