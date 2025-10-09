from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class get_positions(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], department_id: str = None) -> str:
        positions = data.get("positions", [])
        filtered = [
            p
            for p in positions
            if (not department_id or p.get("department_id") == department_id)
        ]
        payload = filtered
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getPositions",
                "description": "Return a list of all positions, optionally filtered by department_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "department_id": {
                            "type": "string",
                            "description": "Department ID to filter positions",
                        }
                    },
                    "required": [],
                    "additionalProperties": False,
                },
            },
        }
