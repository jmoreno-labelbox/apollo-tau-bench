from tau_bench.envs.tool import Tool
import json
import random
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class FindOrdersByCarrier(Tool):
    """Identifies all outbound orders allocated to a specific carrier, filtered by status."""

    @staticmethod
    def invoke(data: dict[str, Any], carrier_name: str = None, status: str = None) -> str:
        if not carrier_name:
            payload = {"error": "carrier_name is a required argument."}
            out = json.dumps(
                payload, indent=2
            )
            return out
        orders = data.get("outbound_orders", {}).values()
        results = [
            o
            for o in orders.values() if o.get("carrier_name") == carrier_name
            and (not status or o.get("status") == status)
        ]
        payload = results
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FindOrdersByCarrier",
                "description": "Finds all outbound orders assigned to a specific carrier, optionally filtering by status.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "carrier_name": {"type": "string"},
                        "status": {"type": "string"},
                    },
                    "required": ["carrier_name"],
                },
            },
        }
