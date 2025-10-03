from tau_bench.envs.tool import Tool
import json
from typing import Any

class GetGameDetailsByGamePk(Tool):
    """Retrieve a game record using its game_pk."""

    @staticmethod
    def invoke(data: dict[str, Any], game_pk: int = None) -> str:
        #1) Confirm validity
        if game_pk is None:
            payload = {"error": "Missing required field: game_pk"}
            out = json.dumps(payload, indent=2)
            return out

        #2) Retrieve DB
        games: list[dict[str, Any]] = data.get("games", [])

        #3) Lookup for exact matches
        for game in games:
            if game.get("game_pk") == game_pk:
                payload = game
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"No game found with game_pk {game_pk}"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getGameDetailsByGamePk",
                "description": "Fetch a single game's full details by its game_pk.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "game_pk": {
                            "type": "integer",
                            "description": "Exact game primary key to retrieve.",
                        }
                    },
                    "required": ["game_pk"],
                },
            },
        }
