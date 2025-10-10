# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class AddRevisionHistoryEntry(Tool):
    """Adds an entry to the revision history of a translation."""
    @staticmethod
    def invoke(data: Dict[str, Any], notes, translation, translation_id, translator, version) -> str:
        translations = data.get("translations", [])
        for t in translations:
            if t.get("id") == translation_id:
                new_entry = {
                    "version": version,
                    "translation": translation,
                    "timestamp": "2025-01-28T00:00:00Z",
                    "translator": translator,
                    "notes": notes
                }
                t["revision_history"].append(new_entry)
                return json.dumps({"status": "success", "message": "Revision history updated."})
        return json.dumps({"error": f"Translation with ID '{translation_id}' not found."})
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "add_revision_history_entry",
                "description": "Adds an entry to the revision history of a translation.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "translation_id": {"type": "string"},
                        "version": {"type": "integer"},
                        "translation": {"type": "string"},
                        "translator": {"type": "string"},
                        "notes": {"type": "string"}
                    },
                    "required": ["translation_id", "version", "translation", "translator", "notes"],
                },
            },
        }
