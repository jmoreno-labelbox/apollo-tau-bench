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

class GetDepartmentTeams(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], department: str = None) -> str:
        if not department:
            payload = {"error": "department is required"}
            out = json.dumps(payload)
            return out

        teams = data.get("teams", [])
        dept_teams = [team for team in teams if team.get("department") == department]
        payload = dept_teams
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetDepartmentTeams",
                "description": "Get all teams in a department",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "department": {
                            "type": "string",
                            "description": "Department name",
                        }
                    },
                    "required": ["department"],
                },
            },
        }
