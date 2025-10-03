from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta
from typing import Any, Dict

class UpdateOrderStatus(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], order_id: str, new_status: str) -> str:
        orders = data.get("outbound_orders", [])

        order = next((o for o in orders if o.get("order_id") == order_id), None)
        if not order:
            return json.dumps({"error": f"Order {order_id} not found"})

        old_status = order.get("status")
        order["status"] = new_status
        order["last_updated"] = get_current_year_month_day()

        if new_status == "Shipped":
            order["actual_ship_date"] = get_current_year_month_day()

        return json.dumps({
            "order_id": order_id,
            "old_status": old_status,
            "new_status": new_status,
            "updated_timestamp": order["last_updated"]
        })
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateOrderStatus",
                "description": "Update the status of an order",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string", "description": "Order identifier"},
                        "new_status": {"type": "string", "description": "New order status"},
                        "status": {"type": "string", "description": "Alternative status parameter"}
                    },
                    "required": ["order_id", "new_status"]
                }
            }
        }
