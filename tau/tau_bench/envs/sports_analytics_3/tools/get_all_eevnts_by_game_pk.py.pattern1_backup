# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetAllEevntsByGamePk(Tool):
    """
    Return all game-day events for a given game_pk.

    Notes:
      - Exact match on game_pk (no normalization).
      - Results are sorted deterministically by timestamp_utc asc, then event_id asc.
      - Expects the events array under data["game_day_events"].
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        game_pk = kwargs.get("game_pk")

        # 1) Validate
        if game_pk is None:
            return json.dumps({"error": "Missing required field: game_pk"}, indent=2)

        # 2) Get DB from passed-in data
        events: List[Dict[str, Any]] = data.get("game_day_events", [])

        # 3) Filter by exact game_pk
        matching = [e for e in events if e.get("game_pk") == game_pk]

        if not matching:
            return json.dumps({"error": f"No events found for game_pk {game_pk}"}, indent=2)

        # 4) Deterministic ordering
        matching.sort(key=lambda e: (e.get("timestamp_utc", ""), int(e.get("event_id", 0))))

        return json.dumps(matching, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_all_eevnts_by_game_pk",
                "description": "Fetch all game-day events for the specified game_pk (exact match).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "game_pk": {
                            "type": "integer",
                            "description": "Exact game primary key whose events should be returned."
                        }
                    },
                    "required": ["game_pk"]
                }
            }
        }
