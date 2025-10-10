# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import FIXED_NOW


class ConfigureShippingRules(Tool):
    """Configure shipping rules and delivery options."""

    @staticmethod
    def invoke(
        data: Dict[str, Any],
        rule_name: Any,
        shipping_zone: Any,
        customer_id: Any = None,
        tracking_enabled: bool = False,
    ) -> str:
        customer_id = _idstr(customer_id) if customer_id is not None else None
        try:
            tracking_enabled = (
                bool(tracking_enabled)
                if isinstance(tracking_enabled, bool)
                else str(tracking_enabled).strip().lower() == "true"
            )
        except Exception:
            tracking_enabled = False

        shipping_zone = shipping_zone or ("US" if customer_id else None)
        if shipping_zone == "US-Standard":
            shipping_zone = "US-Std"

        if not rule_name or not shipping_zone:
            return _error("rule_name and shipping_zone are required.")

        shipping_rules = data.setdefault("shipping_rules", [])
        rule_id = f"SHIP_{len(shipping_rules) + 1:03d}"

        rule = {
            "rule_id": rule_id,
            "rule_name": rule_name,
            "shipping_zone": shipping_zone,
            "tracking_enabled": bool(tracking_enabled),
            "base_cost": 5.99,
            "created_at": FIXED_NOW,
            "status": "active",
        }
        shipping_rules.append(rule)

        result = {
            "rule_id": rule_id,
            "rule_name": rule_name,
            "shipping_zone": shipping_zone,
            "status": "configured",
        }

        return json.dumps(result, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "configure_shipping_rules",
                "description": "Configure shipping rules and delivery options.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "rule_name": {"type": "string"},
                        "tracking_enabled": {"type": "boolean"},
                        "customer_id": {"type": "string"},
                        "shipping_zone": {"type": "string"},
                    },
                    "required": ["rule_name", "shipping_zone"],
                },
            },
        }
