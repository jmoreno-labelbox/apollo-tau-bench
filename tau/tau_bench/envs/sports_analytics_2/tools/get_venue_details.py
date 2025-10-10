# Copyright © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetVenueDetails(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        game_pk = kwargs.get("game_pk")
        game = next((g for g in data.get("games", []) if g.get("game_pk") == int(game_pk)), None)
        venues = data.get("venues", [])
        venue = next((v for v in venues if v.get("venue_id") == (game or {}).get("venue_id")), None)
        return json.dumps(venue or {}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "get_venue_details", "description": "Gets venue details for a game.", "parameters": {"type": "object", "properties": {"game_pk": {"type": "string"}}, "required": ["game_pk"]}}}
