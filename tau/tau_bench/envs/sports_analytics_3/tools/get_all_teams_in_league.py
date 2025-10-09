from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetAllTeamsInLeague(Tool):
    """Retrieve all teams associated with a specific league."""

    @staticmethod
    def invoke(data: dict[str, Any], league: str = None) -> str:
        #1) Confirm validity
        if not isinstance(league, str) or league == "":
            payload = {"error": "Missing required field: league"}
            out = json.dumps(payload, indent=2)
            return out

        #2) Retrieve DB using provided data
        teams: list[dict[str, Any]] = data.get("teams", [])

        #3) Filter teams based on exact league
        matching_teams = [team for team in teams if team.get("league") == league]

        if not matching_teams:
            payload = {"error": f"No teams found in league {league}"}
            out = json.dumps(payload, indent=2)
            return out
        payload = matching_teams
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getAllTeamsInLeague",
                "description": "Fetch all team records belonging to the specified league (exact, case-sensitive).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "league": {
                            "type": "string",
                            "description": "Exact league name to retrieve teams for (e.g., 'American League').",
                        }
                    },
                    "required": ["league"],
                },
            },
        }
