# Sierra copyright.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetUmpireRotation(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        game_pk = kwargs.get("game_pk")
        rotation = [u for u in data.get("umpire_game_models", []) if u.get("game_pk") == int(game_pk)]
        return json.dumps(rotation, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "get_umpire_rotation", "description": "Gets umpire rotation/model rows for a game.", "parameters": {"type": "object", "properties": {"game_pk": {"type": "string"}}, "required": ["game_pk"]}}}
