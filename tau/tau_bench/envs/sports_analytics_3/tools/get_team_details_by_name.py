# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetTeamDetailsByName(Tool):
    """Fetch a team record by its team_name (exact, case-sensitive)."""

    @staticmethod
    def invoke(data: Dict[str, Any], name) -> str:

        # 1) Verify
        if not isinstance(name, str) or name == "":
            return json.dumps({"error": "Missing required field: name"}, indent=2)

        # 2) Retrieve the database from the provided data.
        teams = list(data.get("teams", {}).values())

        # 3) Direct match search (without normalization)
        for team in teams:
            if team.get("team_name") == name:
                return json.dumps(team, indent=2)

        return json.dumps({"error": f"No team found with name {name}"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_team_details_by_name",
                "description": "Fetch a single team's full details by exact team_name (case-sensitive).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "name": {
                            "type": "string",
                            "description": "Exact team name to retrieve."
                        }
                    },
                    "required": ["name"]
                }
            }
        }
