from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetTeamDetailsByName(Tool):
    """Retrieve a team record using its team_name (exact, case-sensitive)."""

    @staticmethod
    def invoke(data: dict[str, Any], name: str = None) -> str:
        #1) Confirm validity
        if not isinstance(name, str) or name == "":
            payload = {"error": "Missing required field: name"}
            out = json.dumps(payload, indent=2)
            return out

        #2) Retrieve DB using provided data
        teams = data.get("teams", [])

        #3) Lookup for exact matches (without normalization)
        for team in teams:
            if team.get("team_name") == name:
                payload = team
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"No team found with name {name}"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetTeamDetailsByName",
                "description": "Fetch a single team's full details by exact team_name (case-sensitive).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "name": {
                            "type": "string",
                            "description": "Exact team name to retrieve.",
                        }
                    },
                    "required": ["name"],
                },
            },
        }
