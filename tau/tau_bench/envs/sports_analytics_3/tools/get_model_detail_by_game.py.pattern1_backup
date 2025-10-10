# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetModelDetailByGame(Tool):
    """
    Fetch per-game umpire model calibration details.

    Input:
      - game_pk (int): Exact game_pk to look up.

    Behavior:
      - Reads from data["umpire_game_models"].
      - Returns all matching rows, sorted deterministically by umpire_game_id ASC.
      - If no match, returns a clear error payload.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        game_pk = kwargs.get("game_pk")

        # 1) Validate
        if game_pk is None:
            return json.dumps({"error": "Missing required field: game_pk"}, indent=2)

        # 2) Get DB
        models: List[Dict[str, Any]] = data.get("umpire_game_models", [])

        # 3) Collect matches
        matches = [row for row in models if row.get("game_pk") == game_pk]

        if not matches:
            return json.dumps({"error": f"No model details found for game_pk {game_pk}"}, indent=2)

        # 4) Deterministic order
        matches.sort(key=lambda r: int(r.get("umpire_game_id", 0)))

        # 5) Return
        return json.dumps(matches, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_model_detail_by_game",
                "description": "Return umpire model calibration details for a given game_pk (sorted by umpire_game_id ASC).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "game_pk": {
                            "type": "integer",
                            "description": "Exact game identifier (game_pk)."
                        }
                    },
                    "required": ["game_pk"]
                }
            }
        }
