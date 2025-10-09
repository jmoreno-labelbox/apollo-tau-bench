from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class ListUserMentorships(Tool):
    @staticmethod
    def invoke(data, user_id: str, user_mentorship_relationships: list = None) -> str:
        if user_mentorship_relationships is None:
            user_mentorship_relationships = data.get("user_mentorship_relationships", {}).values()
        rels = [
            rel
            for rel in user_mentorship_relationships.values() if rel.get("mentee_id") == user_id
        ]
        payload = {"mentorships": rels}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict:
        pass
        return {
            "type": "function",
            "function": {
                "name": "listUserMentorships",
                "description": "List all mentorship relationships for a specific user.",
                "parameters": {
                    "type": "object",
                    "properties": {"user_id": {"type": "string"}},
                    "required": ["user_id"],
                },
            },
        }
