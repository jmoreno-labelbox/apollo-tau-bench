# Copyright © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _find_one


class AnalyzeCustomerBehavior(Tool):
    """Analyze customer purchasing behavior and generate insights."""

    @staticmethod
    def invoke(data: Dict[str, Any], contact_id: Any, analysis_period: Any = "30d") -> str:
        contact_id = _idstr(contact_id)
        analysis_period = f"{analysis_period}"
        if not contact_id:
            return _error("contact_id is required.")

        contacts = data.get("contacts", [])
        contact = _find_one(contacts, "contact_id", contact_id)
        if not contact:
            return _error(f"Contact '{contact_id}' not found.")

        orders = list(data.get("orders", {}).values())
        customer_orders = [o for o in orders if f"{o.get('contact_id')}" == f"{contact_id}"]

        total_orders = len(customer_orders)
        total_value = sum(float(o.get("total_amount", 0.0)) for o in customer_orders)
        avg_order_value = round(total_value / total_orders, 2) if total_orders > 0 else 0.0

        analysis_id = f"ANLY_{contact_id}_{analysis_period}"
        _append_audit(
            data, "customer_behavior_analyzed", analysis_id, {"analysis_period": analysis_period}
        )
        return json.dumps(
            {
                "analysis_id": analysis_id,
                "contact_id": contact_id,
                "analysis_period": analysis_period,
                "total_orders": total_orders,
                "avg_order_value": avg_order_value,
                "preferred_categories": ["Electronics"],
            },
            indent=2,
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "analyze_customer_behavior",
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
