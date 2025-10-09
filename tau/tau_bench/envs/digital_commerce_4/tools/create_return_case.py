from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class CreateReturnCase(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], order_id: str, items: list[dict[str, Any]]) -> str:
        order_id = _sid(order_id)
        orders = data.get("orders", [])
        cases = data.get("cases", [])
        order = next((o for o in orders if o.get("order_id") == order_id), None)
        if not order:
            payload = {"error": f"order {order_id} not found"}
            out = json.dumps(payload, indent=2)
            return out
        if order.get("status") != "Delivered":
            payload = {"error": "returns only allowed for Delivered"}
            out = json.dumps(payload, indent=2)
            return out
        new_case_id = f"5{order_id}"
        cases.append(
            {
                "case_id": new_case_id,
                "contact_id": order.get("contact_id"),
                "account_id": order.get("account_id"),
                "order_id": order_id,
                "subject": f"Return Request for Order #{order_id}",
                "status": "New",
                "priority": "Medium",
            }
        )
        order["status"] = "Return Pending"
        _append_audit(
            data,
            "CREATE_RETURN_CASE",
            order_id,
            {"case_id": new_case_id, "items": items},
        )
        _ws_append(
            data,
            order_id,
            "CREATE_RETURN_CASE",
            {"case_id": new_case_id, "items": items},
        )
        payload = {"case_id": new_case_id, "order_status": order["status"]}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "createReturnCase",
                "description": "Create a return case for a Delivered order and set order to Return Pending.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "order_id": {"type": "string"},
                        "items": {"type": "array", "items": {"type": "object"}},
                    },
                    "required": ["order_id", "items"],
                },
            },
        }
