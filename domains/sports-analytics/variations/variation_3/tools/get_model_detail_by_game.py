from tau_bench.envs.tool import Tool
import json
from typing import Any

class GetModelDetailByGame(Tool):
    """
    Retrieve per-game umpire model calibration details.

    Input:
      - game_pk (int): Exact game_pk to look up.

    Behavior:
      - Reads from data["umpire_game_models"].
      - Returns all matching rows, sorted deterministically by umpire_game_id in ascending order.
      - If no match is found, returns a clear error payload.
    """

    @staticmethod
    def invoke(data: dict[str, Any], game_pk: int = None) -> str:
        #1) Confirm validity
        if game_pk is None:
            payload = {"error": "Missing required field: game_pk"}
            out = json.dumps(payload, indent=2)
            return out

        #2) Retrieve DB
        models: list[dict[str, Any]] = data.get("umpire_game_models", [])

        #3) Gather matches
        matches = [row for row in models if row.get("game_pk") == game_pk]

        if not matches:
            payload = {"error": f"No model details found for game_pk {game_pk}"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        #4) Order deterministically
        matches.sort(key=lambda r: int(r.get("umpire_game_id", 0)))
        payload = matches
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetModelDetailByGame",
                "description": "Return umpire model calibration details for a given game_pk (sorted by umpire_game_id ASC).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "game_pk": {
                            "type": "integer",
                            "description": "Exact game identifier (game_pk).",
                        }
                    },
                    "required": ["game_pk"],
                },
            },
        }
