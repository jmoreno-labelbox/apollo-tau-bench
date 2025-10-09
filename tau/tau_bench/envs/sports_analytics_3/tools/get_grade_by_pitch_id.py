from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetGradeByPitchId(Tool):
    """Retrieve the execution grade record for a specific pitch_id."""

    @staticmethod
    def invoke(data: dict[str, Any], pitch_id: str = None) -> str:
        #1) Confirm validity
        if pitch_id is None:
            payload = {"error": "Missing required field: pitch_id"}
            out = json.dumps(payload, indent=2)
            return out

        #2) Retrieve DB
        grades: list[dict[str, Any]] = data.get("pitch_execution_grades", {}).values()

        #3) Lookup for exact matches
        for rec in grades:
            if rec.get("pitch_id") == pitch_id:
                payload = rec
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"No grade found for pitch_id {pitch_id}"}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getGradeByPitchId",
                "description": "Fetch a single pitch execution grade record by pitch_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "pitch_id": {
                            "type": "integer",
                            "description": "Exact pitch ID whose grade should be returned.",
                        }
                    },
                    "required": ["pitch_id"],
                },
            },
        }
