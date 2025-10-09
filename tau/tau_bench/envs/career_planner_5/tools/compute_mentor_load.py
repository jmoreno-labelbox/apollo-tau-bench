from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class ComputeMentorLoad(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], mentor_id: str) -> str:
        """Calculate the number of active mentees for a mentor."""
        count = sum(
            1
            for rel in data.get("user_mentorship_relationships", [])
            if rel["mentor_id"] == mentor_id and rel["status"] == "Active"
        )
        payload = {"current_mentees": count}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "computeMentorLoad",
                "description": "Return the number of active mentees a mentor currently has.",
                "parameters": {
                    "type": "object",
                    "properties": {"mentor_id": {"type": "string"}},
                    "required": ["mentor_id"],
                },
            },
        }
