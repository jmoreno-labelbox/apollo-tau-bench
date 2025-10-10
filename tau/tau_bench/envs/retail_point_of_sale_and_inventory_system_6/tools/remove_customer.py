# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class remove_customer(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        customers = list(data.get("customers", {}).values())

        customer_id = kwargs.get("customer_id")

        if customer_id is None:
            return json.dumps({"error": "customer_id must be sent"}, indent=2)

        for customer in customers:
            if customer["customer_id"] == customer_id:
                del customer

                return json.dumps(
                    {"success": "Removed customer: {}".format(customer_id)}, indent=2
                )

        return json.dumps({"error": "No customer found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "remove_customer",
                "description": "Removes a customer record",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_id": {
                            "type": "string",
                            "description": "The id of the customer to remove",
                        },
                    },
                },
            },
        }
