from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetGameByHomeAway(Tool):
    """
    Retrieve a single game using exact home/away team IDs.

    Inputs (exact names; case-sensitive):
      - home (int)  : home team ID
      - awy  (int)  : away team ID

    Behavior:
      - Exact match on home_team_id and away_team_id.
      - If multiple games match, return the one with the earliest game_date;
        use smallest game_pk as a tie-breaker for determinism.
      - Returns a structured error if no match is found.
    """

    @staticmethod
    def invoke(data: dict[str, Any], home_id: str = None, away_id: str = None) -> str:
        import json

        home = home_id
        away = away_id

        #1) Confirm required inputs
        missing = []
        if home is None:
            missing.append("home")
        if away is None:
            missing.append("awy")
        if missing:
            payload = {"error": f"Missing required field(s): {', '.join(missing)}"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        #2) Access DB
        games: list[dict[str, Any]] = data.get("games", [])

        #3) Filter for exact matches
        matches = [
            g
            for g in games
            if g.get("home_team_id") == home and g.get("away_team_id") == away
        ]

        if not matches:
            payload = {
                    "error": f"No game found with home_team_id {home} and away_team_id {away}"
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        #4) Deterministic selection: earliest date first, then smallest game_pk
        matches.sort(key=lambda g: (g.get("game_date", ""), int(g.get("game_pk", 0))))
        payload = matches[0]
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetGameByHomeAway",
                "description": "Fetch a single game by exact home and away team IDs. If multiple, returns the earliest by date, then smallest game_pk.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "home_id": {
                            "type": "integer",
                            "description": "Exact home team ID.",
                        },
                        "away_id": {
                            "type": "integer",
                            "description": "Exact away team ID.",
                        },
                    },
                    "required": ["home_id", "away_id"],
                },
            },
        }
