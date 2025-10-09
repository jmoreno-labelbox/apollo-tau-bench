from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetVenueDetails(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], **kwargs) -> str:
        pass
        game_pk = kwargs.get("game_pk")
        game = next(
            (g for g in data.get("games", []) if g.get("game_pk") == int(game_pk)), None
        )
        venues = data.get("venues", [])
        venue = next(
            (v for v in venues if v.get("venue_id") == (game or {}).get("venue_id")),
            None,
        )
        payload = venue or {}
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getVenueDetails",
                "description": "Gets venue details for a game.",
                "parameters": {
                    "type": "object",
                    "properties": {"game_pk": {"type": "string"}},
                    "required": ["game_pk"],
                },
            },
        }
