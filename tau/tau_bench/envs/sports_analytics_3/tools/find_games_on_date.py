# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class FindGamesOnDate(Tool):
    """Fetch all games scheduled on an exact date (YYYY-MM-DD)."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        date = kwargs.get("date")

        # 1) Validate
        if not isinstance(date, str) or date == "":
            return json.dumps({"error": "Missing required field: date (YYYY-MM-DD)"}, indent=2)

        # 2) Get DB
        games: List[Dict[str, Any]] = list(data.get("games", {}).values())

        # 3) Exact match on game_date (no normalization)
        matching = [g for g in games if g.get("game_date") == date]

        if not matching:
            return json.dumps({"error": f"No games found on date {date}"}, indent=2)

        return json.dumps(matching, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "find_games_on_date",
                "description": "Fetch all games that have game_date equal to the given date (exact match).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "date": {
                            "type": "string",
                            "description": "Target date in YYYY-MM-DD (exact match against game_date)."
                        }
                    },
                    "required": ["date"]
                }
            }
        }
