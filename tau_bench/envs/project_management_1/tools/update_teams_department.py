from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime
from typing import Any

class UpdateTeamsDepartment(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], team_id: str = None, department: str = None) -> str:
        if not all([team_id, department]):
            payload = {"error": "team_id and department are required"}
            out = json.dumps(payload)
            return out

        teams = data.get("teams", [])

        for team in teams:
            if team.get("team_id") == team_id:
                team["department"] = department
                payload = {"success": True, "team": team}
                out = json.dumps(payload)
                return out
        payload = {"error": f"Employee with ID '{team_id}' not found"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateTeamsDepartment",
                "description": "Update team department",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "team_id": {
                            "type": "string",
                            "description": "The team ID",
                        },
                        "department": {
                            "type": "string",
                            "description": "New department",
                        },
                    },
                    "required": ["team_id", "department"],
                },
            },
        }
