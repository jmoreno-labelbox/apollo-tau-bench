from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class ListMentorshipRelationships(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        filters: Any = None,
        mentor_id: str = None,
        status: str = None
    ) -> str:
        relationships = data.get("user_mentorship_relationships", {}).values()
        if mentor_id is not None:
            relationships = [
                r for r in relationships.values() if r.get("mentor_id") == mentor_id
            ]
        if status is not None:
            relationships = [
                r for r in relationships.values() if r.get("status") == status
            ]
        payload = {"relationships": relationships}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict:
        pass
        return {
            "type": "function",
            "function": {
                "name": "listMentorshipRelationships",
                "description": "List mentorship relationships by filters",
                "parameters": {
                    "type": "object",
                    "properties": {"filters": {"type": "object"}},
                    "required": ["filters"],
                },
            },
        }
