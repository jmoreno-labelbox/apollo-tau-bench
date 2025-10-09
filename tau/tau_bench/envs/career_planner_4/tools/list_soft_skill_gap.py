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

class ListSoftSkillGap(Tool):
    @staticmethod
    def invoke(data, user_id: str, skill: str) -> str:
        analyses = [
            a
            for a in data.get("skill_gap_analysis", {}).values()
            if a.get("skill") == skill and a.get("user_id") == user_id
        ]
        payload = {"soft_skill_gap": analyses}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict:
        pass
        return {
            "type": "function",
            "function": {
                "name": "listSoftSkillGap",
                "description": "List soft skill gap analysis records for a user for a specific skill.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string"},
                        "skill": {"type": "string"},
                    },
                    "required": ["user_id", "skill"],
                },
            },
        }
