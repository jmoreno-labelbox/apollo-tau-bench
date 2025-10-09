from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetTeamMembers(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], team_id: str = None) -> str:
        teams = data.get("teams", [])

        for t in teams:
            if t["team_id"] == team_id:
                payload = {"user_ids": t.get("team_members", [])}
                out = json.dumps(payload, indent=2)
                return out
        payload = {
                "error": "Team not found",
                "team_id": team_id,
                "available_teams": [t["team_id"] for t in teams],
            }
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetTeamMembers",
                "description": "Returns a list of user IDs belonging to a specific team.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "team_id": {
                            "type": "string",
                            "description": "The team ID to search for.",
                        }
                    },
                    "required": ["team_id"],
                },
            },
        }
