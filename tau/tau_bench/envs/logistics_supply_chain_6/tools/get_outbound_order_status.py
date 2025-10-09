from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetOutboundOrderStatus(Tool):
    """Utility for checking the status of an outbound order."""

    @staticmethod
    def invoke(data: dict[str, Any], order_id: str) -> str:
        """Run the tool using the specified parameters."""
        orders = data.get("outbound_orders", [])
        for order in orders:
            if order.get("order_id") == order_id:
                payload = order
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"Order with ID {order_id} not found"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        """Provide specifications of the tool for the AI agent."""
        pass
        return {
            "type": "function",
            "function": {
                "name": "GetOutboundOrderStatus",
                "description": "Retrieves the current status and details of a specific outbound customer order.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {
                            "type": "string",
                            "description": "The ID of the order to look up.",
                        }
                    },
                    "required": ["order_id"],
                },
            },
        }
