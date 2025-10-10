# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateNewGame(Tool):
    """
    Create a new game row.
      Inputs (exact names):
        - date (YYYY-MM-DD)
        - venue_id (int)
        - home_team_id (int)
        - away_team_id (int)
      Behavior:
        - game_pk is generated automatically (max existing game_pk + 1; starts at 1 if empty).
        - game_status defaults to "Scheduled".
        - final_score and attendance default to null.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        date = kwargs.get("date")
        venue_id = kwargs.get("venue_id")
        home_team_id = kwargs.get("home_team_id")
        away_team_id = kwargs.get("away_team_id")

        # 1) Validate required inputs
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
            return json.dumps({"error": f"Missing required field(s): {', '.join(missing)}"}, indent=2)

        # 2) Get DB from passed-in data
        games: List[Dict[str, Any]] = data.get("games", [])

        # 3) Generate a new unique game_pk deterministically from DB state
        

        # 4) Create the new game row with defaults
        new_row = {
            "game_pk": get_next_game_id(data),
            "game_date": date,
            "venue_id": venue_id,
            "home_team_id": home_team_id,
            "away_team_id": away_team_id,
            "game_status": "Scheduled",
            "final_score": None,
            "attendance": None
        }

        # 5) Insert
        games.append(new_row)

        return json.dumps(new_row, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_new_game",
                "description": (
                    "Create a new game. Generates game_pk automatically (max existing + 1). "
                    "Defaults game_status to 'Scheduled'."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "date": {
                            "type": "string",
                            "description": "Game date in YYYY-MM-DD."
                        },
                        "venue_id": {
                            "type": "integer",
                            "description": "Venue ID."
                        },
                        "home_team_id": {
                            "type": "integer",
                            "description": "Home team ID."
                        },
                        "away_team_id": {
                            "type": "integer",
                            "description": "Away team ID."
                        }
                    },
                    "required": ["date", "venue_id", "home_team_id", "away_team_id"]
                }
            }
        }
