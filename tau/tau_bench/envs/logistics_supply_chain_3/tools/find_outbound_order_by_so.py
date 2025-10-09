from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class FindOutboundOrderBySO(Tool):
    """Locates a single outbound order record using its Sales Order (SO) number."""

    @staticmethod
    def invoke(data: dict[str, Any], sales_order_number: str = None, outbound_orders: list = None) -> str:
        outbound_orders = outbound_orders if outbound_orders is not None else data.get("outbound_orders", {}).values()
        for order in outbound_orders:
            if order.get("sales_order_number") == sales_order_number:
                payload = order
                out = json.dumps(payload)
                return out
        payload = {"error": "Outbound order not found for that Sales Order number"}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FindOutboundOrderBySo",
                "description": "Finds the full details of an outbound order using its Sales Order (SO) number.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "sales_order_number": {
                            "type": "string",
                            "description": "The Sales Order number of the order to find (e.g., 'SO-2024-0002').",
                        }
                    },
                    "required": ["sales_order_number"],
                },
            },
        }
