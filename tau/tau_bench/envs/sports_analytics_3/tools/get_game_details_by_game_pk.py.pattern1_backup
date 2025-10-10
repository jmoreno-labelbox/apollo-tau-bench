# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetGameDetailsByGamePk(Tool):
    """Fetch a game record by its game_pk."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        game_pk = kwargs.get("game_pk")

        # 1) Validate
        if game_pk is None:
            return json.dumps({"error": "Missing required field: game_pk"}, indent=2)

        # 2) Get DB
        games: List[Dict[str, Any]] = data.get("games", [])

        # 3) Exact match lookup
        for game in games:
            if game.get("game_pk") == game_pk:
                return json.dumps(game, indent=2)

        return json.dumps({"error": f"No game found with game_pk {game_pk}"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_game_details_by_game_pk",
                "description": "Fetch a single game's full details by its game_pk.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "game_pk": {
                            "type": "integer",
                            "description": "Exact game primary key to retrieve."
                        }
                    },
                    "required": ["game_pk"]
                }
            }
        }
