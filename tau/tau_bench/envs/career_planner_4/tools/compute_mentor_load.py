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

class ComputeMentorLoad(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], mentor_id: str) -> str:
        relationships = [
            r
            for r in data.get("user_mentorship_relationships", {}).values()
            if r.get("mentor_id") == mentor_id and r.get("status") == "Active"
        ]
        load = len(relationships)
        payload = {"mentor_load": load, "mentor_id": mentor_id}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict:
        pass
        return {
            "type": "function",
            "function": {
                "name": "computeMentorLoad",
                "description": "Compute the current active mentee load for a mentor",
                "parameters": {
                    "type": "object",
                    "properties": {"mentor_id": {"type": "string"}},
                    "required": ["mentor_id"],
                },
            },
        }
