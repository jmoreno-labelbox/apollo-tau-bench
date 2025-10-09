from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class FindGamesOnDate(Tool):
    """Retrieve all games planned for a specific date (YYYY-MM-DD)."""

    @staticmethod
    def invoke(data: dict[str, Any], date: str = None) -> str:
        #1) Confirm validity
        if not isinstance(date, str) or date == "":
            payload = {"error": "Missing required field: date (YYYY-MM-DD)"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        #2) Retrieve DB
        games: list[dict[str, Any]] = data.get("games", {}).values()

        #3) Exact match on game_date (without normalization)
        matching = [g for g in games.values() if g.get("game_date") == date]

        if not matching:
            payload = {"error": f"No games found on date {date}"}
            out = json.dumps(payload, indent=2)
            return out
        payload = matching
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FindGamesOnDate",
                "description": "Fetch all games that have game_date equal to the given date (exact match).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "date": {
                            "type": "string",
                            "description": "Target date in YYYY-MM-DD (exact match against game_date).",
                        }
                    },
                    "required": ["date"],
                },
            },
        }
