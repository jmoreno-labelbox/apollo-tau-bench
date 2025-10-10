# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetGameByHomeAway(Tool):
    """
    Fetch a single game by exact home/away team IDs.

    Inputs (exact names; case-sensitive):
      - home (int)  : home team ID
      - awy  (int)  : away team ID

    Behavior:
      - Exact match on home_team_id and away_team_id.
      - If multiple games match, return the one with the earliest game_date;
        tie-break by smallest game_pk for determinism.
      - Returns a structured error if no match is found.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        import json

        home = kwargs.get("home_id")
        away = kwargs.get("away_id")

        # 1) Validate required inputs
        missing = []
        if home is None:
            missing.append("home")
        if away is None:
            missing.append("awy")
        if missing:
            return json.dumps({"error": f"Missing required field(s): {', '.join(missing)}"}, indent=2)

        # 2) Access DB
        games: List[Dict[str, Any]] = data.get("games", [])

        # 3) Filter by exact match
        matches = [
            g for g in games
            if g.get("home_team_id") == home and g.get("away_team_id") == away
        ]

        if not matches:
            return json.dumps(
                {"error": f"No game found with home_team_id {home} and away_team_id {away}"},
                indent=2
            )

        # 4) Deterministic selection: earliest date, then smallest game_pk
        matches.sort(key=lambda g: (g.get("game_date", ""), int(g.get("game_pk", 0))))
        return json.dumps(matches[0], indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_game_by_home_away",
                "description": "Fetch a single game by exact home and away team IDs. If multiple, returns the earliest by date, then smallest game_pk.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "home_id": {
                            "type": "integer",
                            "description": "Exact home team ID."
                        },
                        "away_id": {
                            "type": "integer",
                            "description": "Exact away team ID."
                        }
                    },
                    "required": ["home_id", "away_id"]
                }
            }
        }
