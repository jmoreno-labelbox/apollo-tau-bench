from tau_bench.envs.tool import Tool
import json
from datetime import date, timedelta
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class UpdateOrderStatus(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], order_id: str = None, new_status: str = "placed") -> str:
        if order_id is None:
            household_id = _default_household_id(data, _first_user_id(data))
            order_id = _latest_order_id(data, household_id)
        order = next(
            (o for o in data.get("orders", []) if o.get("order_id") == order_id), None
        )
        if not order:
            return _json_dump({"error": "no order available"})
        order["status_enum"] = str(new_status)
        return _json_dump(order)
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateOrderStatus",
                "description": "Update order status; defaults to latest order and status 'placed'.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "integer"},
                        "new_status": {"type": "string"},
                    },
                    "required": [],
                },
            },
        }
