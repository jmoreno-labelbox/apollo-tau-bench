from tau_bench.envs.tool import Tool
import json
from typing import Any

class GetTeamDetailsById(Tool):
    """Retrieve a team record using its team_id."""

    @staticmethod
    def invoke(data: dict[str, Any], team_id: str = None) -> str:
        #1) Confirm validity
        if team_id is None:
            payload = {"error": "Missing required field: team_id"}
            out = json.dumps(payload, indent=2)
            return out

        #2) Retrieve DB using provided data
        teams = data.get("teams", [])

        #3) Lookup for exact matches
        for team in teams:
            if team.get("team_id") == team_id:
                payload = team
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"No team found with ID {team_id}"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetTeamDetailsById",
                "description": "Fetch a single team's full details by its team_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "team_id": {
                            "type": "integer",
                            "description": "Exact team ID to retrieve.",
                        }
                    },
                    "required": ["team_id"],
                },
            },
        }
