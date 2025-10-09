from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetPitchDetailsById(Tool):
    """Retrieve a single pitch using its pitch_id."""

    @staticmethod
    def invoke(data: dict[str, Any], pitch_id: str = None) -> str:
        #1) Confirm validity
        if pitch_id is None:
            payload = {"error": "Missing required field: pitch_id"}
            out = json.dumps(payload, indent=2)
            return out

        #2) Retrieve DB
        pitches: list[dict[str, Any]] = data.get("pitches", [])

        #3) Lookup for exact matches
        for p in pitches:
            if p.get("pitch_id") == pitch_id:
                payload = p
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"No pitch found with pitch_id {pitch_id}"}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getPitchDetailsById",
                "description": "Fetch a single pitch's full details by pitch_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "pitch_id": {
                            "type": "integer",
                            "description": "Exact pitch ID to retrieve.",
                        }
                    },
                    "required": ["pitch_id"],
                },
            },
        }
