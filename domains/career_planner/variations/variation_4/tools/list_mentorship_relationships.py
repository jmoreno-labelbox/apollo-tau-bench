from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime
from typing import Any

class ListMentorshipRelationships(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        filters: Any = None,
        mentor_id: str = None,
        status: str = None
    ) -> str:
        relationships = data.get("user_mentorship_relationships", [])
        if mentor_id is not None:
            relationships = [
                r for r in relationships if r.get("mentor_id") == mentor_id
            ]
        if status is not None:
            relationships = [
                r for r in relationships if r.get("status") == status
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
