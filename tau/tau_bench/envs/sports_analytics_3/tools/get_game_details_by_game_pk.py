# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetGameDetailsByGamePk(Tool):
    """Fetch a game record by its game_pk."""

    @staticmethod
    def invoke(data: Dict[str, Any], game_pk) -> str:

        # 1) Confirm validity
        if game_pk is None:
            return json.dumps({"error": "Missing required field: game_pk"}, indent=2)

        # Retrieve database.
        games: List[Dict[str, Any]] = list(data.get("games", {}).values())

        # 3) Precise match retrieval
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
