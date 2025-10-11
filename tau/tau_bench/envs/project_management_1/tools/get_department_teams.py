# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetDepartmentTeams(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], department) -> str:
        if not department:
            return json.dumps({"error": "department is required"})

        teams = data.get("teams", [])
        dept_teams = [team for team in teams if team.get("department") == department]

        return json.dumps(dept_teams, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_department_teams",
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
