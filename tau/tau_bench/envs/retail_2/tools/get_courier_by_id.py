from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetCourierById(Tool):
    """Obtain courier information from couriers.json using courier_id."""

    @staticmethod
    def invoke(data: dict[str, Any], courier_id: str) -> str:
        couriers = data.get("couriers", [])
        for c in couriers:
            if c.get("courier_id") == courier_id:
                payload = c
                out = json.dumps(payload)
                return out
        payload = {"error": "Courier not found", "courier_id": courier_id}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetCourierById",
                "description": "Get courier details from couriers.json by courier_id.",
                "parameters": {
                    "type": "object",
                    "properties": {"courier_id": {"type": "string"}},
                    "required": ["courier_id"],
                },
            },
        }
