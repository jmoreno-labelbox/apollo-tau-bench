# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class update_mentorship_note(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], mentor_id: str, mentee_id: str, note: str) -> str:
        note_record = {
            "mentor_id": mentor_id,
            "mentee_id": mentee_id,
            "note": note,
            "date": "2025-07-04",
        }
        data.setdefault("mentorship_notes", []).append(note_record)
        return json.dumps({"success": "Note added to mentorship record"}, indent=2)

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "update_mentorship_note",
                "description": "Add a note to a mentorship record",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "mentor_id": {"type": "string"},
                        "mentee_id": {"type": "string"},
                        "note": {"type": "string"},
                    },
                    "required": ["mentor_id", "mentee_id", "note"],
                },
            },
        }
