from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime
from typing import Any

class UpdateMentorshipNote(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], mentor_id: str, mentee_id: str, note: str) -> str:
        note_record = {
            "mentor_id": mentor_id,
            "mentee_id": mentee_id,
            "note": note,
            "date": "2025-07-04",
        }
        data.setdefault("mentorship_notes", []).append(note_record)
        payload = {"success": "Note added to mentorship record"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict:
        pass
        return {
            "type": "function",
            "function": {
                "name": "updateMentorshipNote",
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
