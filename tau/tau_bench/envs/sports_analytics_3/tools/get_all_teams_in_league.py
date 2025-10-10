# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetAllTeamsInLeague(Tool):
    """Fetch all teams belonging to a given league."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        league = kwargs.get("league")

        # 1) Validate
        if not isinstance(league, str) or league == "":
            return json.dumps({"error": "Missing required field: league"}, indent=2)

        # 2) Get DB from passed-in data
        teams: List[Dict[str, Any]] = list(data.get("teams", {}).values())

        # 3) Filter teams by exact league
        matching_teams = [
            team for team in teams
            if team.get("league") == league
        ]

        if not matching_teams:
            return json.dumps({"error": f"No teams found in league {league}"}, indent=2)

        return json.dumps(matching_teams, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_all_teams_in_league",
                "description": "Fetch all team records belonging to the specified league (exact, case-sensitive).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "league": {
                            "type": "string",
                            "description": "Exact league name to retrieve teams for (e.g., 'American League')."
                        }
                    },
                    "required": ["league"]
                }
            }
        }
