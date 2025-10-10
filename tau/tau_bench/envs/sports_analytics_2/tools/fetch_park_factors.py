# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class FetchParkFactors(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], game_pk) -> str:
        game = next((g for g in data.get("games", []) if g.get("game_pk") == int(game_pk)), None)
        venue = next((v for v in data.get("venues", []) if v.get("venue_id") == (game or {}).get("venue_id")), None)
        if not venue:
            return json.dumps({}, indent=2)
        return json.dumps({"park_factor_runs": venue.get("park_factor_runs"), "park_factor_hr": venue.get("park_factor_hr")}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "fetch_park_factors", "description": "Fetches park factors for a game's venue.", "parameters": {"type": "object", "properties": {"game_pk": {"type": "string"}}, "required": ["game_pk"]}}}
