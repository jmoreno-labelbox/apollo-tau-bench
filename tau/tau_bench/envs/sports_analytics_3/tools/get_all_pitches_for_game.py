# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetAllPitchesForGame(Tool):
    """Fetch all pitches for a given game_pk."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        game_pk = kwargs.get("game_pk")

        # 1) Validate
        if game_pk is None:
            return json.dumps({"error": "Missing required field: game_pk"}, indent=2)

        # 2) Get DB
        pitches: List[Dict[str, Any]] = data.get("pitches", [])

        # 3) Filter and deterministic order within game
        result = [p for p in pitches if p.get("game_pk") == game_pk]
        if not result:
            return json.dumps({"error": f"No pitches found for game_pk {game_pk}"}, indent=2)

        result.sort(key=lambda p: (p.get("at_bat_index", 0), p.get("pitch_number", 0), p.get("pitch_id", 0)))
        return json.dumps(result, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_all_pitches_for_game",
                "description": "Fetch all pitches belonging to a specific game_pk.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "game_pk": {"type": "integer", "description": "Exact game primary key."}
                    },
                    "required": ["game_pk"]
                }
            }
        }
