from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetAllEevntsByGamePk(Tool):
    """
    Retrieve all game-day events for a specified game_pk.

    Notes:
      - Exact match on game_pk (without normalization).
      - Results are sorted deterministically by timestamp_utc ascending, then event_id ascending.
      - Expects the events array within data["game_day_events"].
    """

    @staticmethod
    def invoke(data: dict[str, Any], game_pk: int = None) -> str:
        #1) Confirm validity
        if game_pk is None:
            payload = {"error": "Missing required field: game_pk"}
            out = json.dumps(payload, indent=2)
            return out

        #2) Retrieve DB using provided data
        events: list[dict[str, Any]] = data.get("game_day_events", {}).values()

        #3) Filter for exact game_pk
        matching = [e for e in events.values() if e.get("game_pk") == game_pk]

        if not matching:
            payload = {"error": f"No events found for game_pk {game_pk}"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        #4) Order deterministically
        matching.sort(
            key=lambda e: (e.get("timestamp_utc", ""), int(e.get("event_id", 0)))
        )
        payload = matching
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getAllEevntsByGamePk",
                "description": "Fetch all game-day events for the specified game_pk (exact match).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "game_pk": {
                            "type": "integer",
                            "description": "Exact game primary key whose events should be returned.",
                        }
                    },
                    "required": ["game_pk"],
                },
            },
        }
