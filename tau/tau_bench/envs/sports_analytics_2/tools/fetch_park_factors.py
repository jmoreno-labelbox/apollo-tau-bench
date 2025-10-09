from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class FetchParkFactors(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], **kwargs) -> str:
        pass
        game_pk = kwargs.get("game_pk")
        game = next(
            (g for g in data.get("games", {}).values() if g.get("game_pk") == int(game_pk)), None
        )
        venue = next(
            (
                v
                for v in data.get("venues", {}).values()
                if v.get("venue_id") == (game or {}).get("venue_id")
            ),
            None,
        )
        if not venue:
            payload = {}
            out = json.dumps(payload, indent=2)
            return out
        payload = {
                "park_factor_runs": venue.get("park_factor_runs"),
                "park_factor_hr": venue.get("park_factor_hr"),
            }
        out = json.dumps(
            payload, indent=2,
        )
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "fetchParkFactors",
                "description": "Fetches park factors for a game's venue.",
                "parameters": {
                    "type": "object",
                    "properties": {"game_pk": {"type": "string"}},
                    "required": ["game_pk"],
                },
            },
        }
