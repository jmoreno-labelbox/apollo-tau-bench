from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class ListMentoringSessions(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], mentee_id: str) -> str:
        sessions = [
            s
            for s in data.get("mentoring_sessions", [])
            if s.get("mentee_id") == mentee_id
        ]
        payload = {"sessions": sessions}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict:
        pass
        return {
            "type": "function",
            "function": {
                "name": "listMentoringSessions",
                "description": "List mentoring sessions for a mentee",
                "parameters": {
                    "type": "object",
                    "properties": {"mentee_id": {"type": "string"}},
                    "required": ["mentee_id"],
                },
            },
        }
