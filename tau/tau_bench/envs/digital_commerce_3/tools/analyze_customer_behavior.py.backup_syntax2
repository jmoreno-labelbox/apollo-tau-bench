from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class AnalyzeCustomerBehavior(Tool):
    """Examine customer buying patterns and produce insights."""

    @staticmethod
    def invoke(
        data: dict[str, Any], contact_id: Any, analysis_period: Any = "30d"
    ) -> str:
        contact_id = _idstr(contact_id)
        analysis_period = f"{analysis_period}"
        if not contact_id:
            return _error("contact_id is required.")

        contacts = data.get("contacts", {}).values()
        contact = _find_one(list(contacts.values()), "contact_id", contact_id)
        if not contact:
            return _error(f"Contact '{contact_id}' not found.")

        orders = data.get("orders", {}).values()
        customer_orders = [
            o for o in orders.values() if f"{o.get('contact_id')}" == f"{contact_id}"
        ]

        total_orders = len(customer_orders)
        total_value = sum(float(o.get("total_amount", 0.0)) for o in customer_orders.values()
        avg_order_value = ()
            round(total_value / total_orders, 2) if total_orders > 0 else 0.0
        )

        analysis_id = f"ANLY_{contact_id}_{analysis_period}"
        _append_audit(
            data,
            "customer_behavior_analyzed",
            analysis_id,
            {"analysis_period": analysis_period},
        )
        payload = {
                "analysis_id": analysis_id,
                "contact_id": contact_id,
                "analysis_period": analysis_period,
                "total_orders": total_orders,
                "avg_order_value": avg_order_value,
                "preferred_categories": ["Electronics"],
            }
        out = json.dumps(
            payload, indent=2,
        )
        return out
        pass
        contact_id = _idstr(contact_id)
        analysis_period = f"{analysis_period}"
        if not contact_id:
            return _error("contact_id is required.")

        contacts = data.get("contacts", {}).values()
        contact = _find_one(list(contacts.values()), "contact_id", contact_id)
        if not contact:
            return _error(f"Contact '{contact_id}' not found.")

        orders = data.get("orders", {}).values()
        customer_orders = [
            o for o in orders.values() if f"{o.get('contact_id')}" == f"{contact_id}"
        ]

        total_orders = len(customer_orders)
        total_value = sum(float(o.get("total_amount", 0.0)) for o in customer_orders.values()
        avg_order_value = (
            round(total_value / total_orders, 2) if total_orders > 0 else 0.0
        )

        analysis_id = f"ANLY_{contact_id}_{analysis_period}"
        _append_audit(
            data,
            "customer_behavior_analyzed",
            analysis_id,
            {"analysis_period": analysis_period},
        )
        payload = {
                "analysis_id": analysis_id,
                "contact_id": contact_id,
                "analysis_period": analysis_period,
                "total_orders": total_orders,
                "avg_order_value": avg_order_value,
                "preferred_categories": ["Electronics"],
            }
        out = json.dumps(
            payload, indent=2,
        )
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AnalyzeCustomerBehavior",
                "description": "Analyze customer purchasing behavior and generate insights.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "contact_id": {"type": "string"},
                        "analysis_period": {"type": "string"},
                    },
                    "required": ["contact_id"],
                },
            },
        }
