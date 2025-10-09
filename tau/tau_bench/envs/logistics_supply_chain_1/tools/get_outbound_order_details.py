from tau_bench.envs.tool import Tool
import json
import random
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetOutboundOrderDetails(Tool):
    """Fetches complete details for a single outbound order using its ID."""

    @staticmethod
    def invoke(data: dict[str, Any], order_id: str = None) -> str:
        if not order_id:
            payload = {"error": "order_id is required."}
            out = json.dumps(payload, indent=2)
            return out
        order = next(
            (
                o
                for o in data.get("outbound_orders", {}).values()
                if o.get("order_id") == order_id
            ),
            None,
        )
        if not order:
            payload = {"error": f"Order '{order_id}' not found."}
            out = json.dumps(payload, indent=2)
            return out
        payload = order
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetOutboundOrderDetails",
                "description": "Retrieves the full details for a single outbound order by its ID.",
                "parameters": {
                    "type": "object",
                    "properties": {"order_id": {"type": "string"}},
                    "required": ["order_id"],
                },
            },
        }
