from tau_bench.envs.tool import Tool
import json
from typing import Any

class GetUmpireRotation(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], **kwargs) -> str:
        pass
        game_pk = kwargs.get("game_pk")
        rotation = [
            u
            for u in data.get("umpire_game_models", [])
            if u.get("game_pk") == int(game_pk)
        ]
        payload = rotation
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getUmpireRotation",
                "description": "Gets umpire rotation/model rows for a game.",
                "parameters": {
                    "type": "object",
                    "properties": {"game_pk": {"type": "string"}},
                    "required": ["game_pk"],
                },
            },
        }
