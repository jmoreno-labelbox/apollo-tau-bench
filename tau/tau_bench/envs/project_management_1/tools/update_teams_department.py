# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateTeamsDepartment(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], department, team_id) -> str:

        if not all([team_id, department]):
            return json.dumps({"error": "team_id and department are required"})

        teams = data.get("teams", [])

        for team in teams:
            if team.get("team_id") == team_id:
                team["department"] = department
                return json.dumps({"success": True, "team": team})

        return json.dumps({"error": f"Employee with ID '{team_id}' not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_teams_department",
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
