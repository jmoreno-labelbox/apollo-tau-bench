from tau_bench.envs.tool import Tool
import json
from typing import Any

class CreateNewGame(Tool):
    """
    Establish a new game row.
      Inputs (exact names):
        - date (YYYY-MM-DD)
        - venue_id (int)
        - home_team_id (int)
        - away_team_id (int)
      Behavior:
        - game_pk is automatically generated (max existing game_pk + 1; starts at 1 if none).
        - game_status defaults to "Scheduled".
        - final_score and attendance default to null.
    """

    @staticmethod
    def invoke(data: dict[str, Any], date: str = None, venue_id: int = None, home_team_id: int = None, away_team_id: int = None) -> str:
        #1) Confirm required inputs
        missing = []
        if not isinstance(date, str) or date == "":
            missing.append("date")
        if venue_id is None:
            missing.append("venue_id")
        if home_team_id is None:
            missing.append("home_team_id")
        if away_team_id is None:
            missing.append("away_team_id")

        if missing:
            payload = {"error": f"Missing required field(s): {', '.join(missing)}"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        #2) Retrieve DB using provided data
        games: list[dict[str, Any]] = data.get("games", [])

        #3) Create a new unique game_pk in a deterministic manner based on DB state

        #4) Establish the new game row with default values
        new_row = {
            "game_pk": get_next_game_id(data),
            "game_date": date,
            "venue_id": venue_id,
            "home_team_id": home_team_id,
            "away_team_id": away_team_id,
            "game_status": "Scheduled",
            "final_score": None,
            "attendance": None,
        }

        #5) Add
        games.append(new_row)
        payload = new_row
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "createNewGame",
                "description": (
                    "Create a new game. Generates game_pk automatically (max existing + 1). "
                    "Defaults game_status to 'Scheduled'."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "date": {
                            "type": "string",
                            "description": "Game date in YYYY-MM-DD.",
                        },
                        "venue_id": {"type": "integer", "description": "Venue ID."},
                        "home_team_id": {
                            "type": "integer",
                            "description": "Home team ID.",
                        },
                        "away_team_id": {
                            "type": "integer",
                            "description": "Away team ID.",
                        },
                    },
                    "required": ["date", "venue_id", "home_team_id", "away_team_id"],
                },
            },
        }
