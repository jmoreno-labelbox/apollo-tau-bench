from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetAllPitchesForGame(Tool):
    """Retrieve all pitches associated with a specific game_pk."""

    @staticmethod
    def invoke(data: dict[str, Any], game_pk: int = None) -> str:
        #1) Confirm validity
        if game_pk is None:
            payload = {"error": "Missing required field: game_pk"}
            out = json.dumps(payload, indent=2)
            return out

        #2) Retrieve DB
        pitches: list[dict[str, Any]] = data.get("pitches", [])

        #3) Filter and order deterministically within the game
        result = [p for p in pitches if p.get("game_pk") == game_pk]
        if not result:
            payload = {"error": f"No pitches found for game_pk {game_pk}"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        result.sort(
            key=lambda p: (
                p.get("at_bat_index", 0),
                p.get("pitch_number", 0),
                p.get("pitch_id", 0),
            )
        )
        payload = result
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetAllPitchesForGame",
                "description": "Fetch all pitches belonging to a specific game_pk.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "game_pk": {
                            "type": "integer",
                            "description": "Exact game primary key.",
                        }
                    },
                    "required": ["game_pk"],
                },
            },
        }
