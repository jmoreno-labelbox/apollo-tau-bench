# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateCustomerMembershipLevel(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], customer_id: str, new_membership_level: str) -> str:
        customers = list(data.get("customers", {}).values())
        valid_levels = ["bronze", "silver", "gold", "platinum", "VIP"]

        if new_membership_level.lower() not in valid_levels:
            return json.dumps({"error": f"Invalid membership level. Valid levels are: {', '.join(valid_levels)}"})

        for i, customer in enumerate(customers):
            if customer.get("customer_id") == customer_id:
                customers[i]["membership_level"] = new_membership_level.lower()
                data["customers"] = customers
                return json.dumps(customers[i], indent=2)
        return json.dumps({"error": f"Customer with ID {customer_id} not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_customer_membership_level",
                "description": "Update membership level for a specific customer.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_id": {"type": "string", "description": "Unique identifier of the customer."},
                        "new_membership_level": {"type": "string", "description": "New membership level."}
                    },
                    "required": ["customer_id", "new_membership_level"]
                }
            }
        }
