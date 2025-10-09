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

class MarkSprintAsReviewed(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], sprint_id: str = None) -> str:
        if not sprint_id:
            payload = {"error": "sprint_id is a required parameter"}
            out = json.dumps(payload)
            return out

        sprints = data.get("sprints", [])

        for sprint in sprints:
            if sprint.get("sprint_id") == sprint_id:
                sprint["reviewed"] = "True"
                payload = {"success": True}
                out = json.dumps(payload)
                return out
        payload = {"error": f"It wasn't found any sprint with the if {sprint_id}"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "MarkSprintAsReviewed",
                "description": "Mark sprint as reviewed",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "sprint_id": {
                            "type": "string",
                            "description": "Id of the sprint",
                        },
                    },
                    "required": [
                        "sprint_id",
                    ],
                },
            },
        }
