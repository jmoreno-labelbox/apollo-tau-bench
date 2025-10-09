from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class get_position(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], position_id: str) -> str:
        positions = data.get("positions", {}).values()
        for p in positions.values():
            if p["position_id"] == position_id:
                payload = p
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"position_id {position_id} not found"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getPosition",
                "description": "Return the position record for the given position_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "position_id": {
                            "type": "string",
                            "description": "Unique ID of the position to fetch",
                        }
                    },
                    "required": ["position_id"],
                    "additionalProperties": False,
                },
            },
        }
