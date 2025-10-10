# Copyright © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class update_customer(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        customers = list(data.get("customers", {}).values())

        # These parameters are required for updates.
        row_id = kwargs.get("customer_id")
        timestamp = kwargs.get("timestamp")

        if (row_id is None) or (timestamp is None):
            return json.dumps({"error": "customer_id and timestamp must be sent"})

        # These are the parameters provided for the update.
        updatable_cols = [
            "name",
            "phone_number",
            "email",
            "address",
            "birthdate",
            "membership_level",
            "status",
            "loyalty_points",
            "opt_in_marketing",
        ]
        updating_values = {k: kwargs.get(k) for k in updatable_cols}

        for customer in customers:
            if customer["customer_id"] == row_id:
                for col, value in updating_values.items():
                    # Modify all transmitted values.
                    if value is not None:
                        customer[col] = value

                customer["updated_at"] = timestamp

                return json.dumps(customer, indent=2)

        return json.dumps({"error": "no matching records found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_customer",
                "description": "Creates a new customer record",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "timestamp": {
                            "type": "string",
                            "description": "The current timestamp. Used for database timestamp rows",
                        },
                        "customer_id": {
                            "type": "string",
                            "description": "REQUIRED. The id of the customer to update",
                        },
                        "name": {
                            "type": "string",
                            "description": "The customer's name",
                        },
                        "phone_number": {
                            "type": "string",
                            "description": "The customer's phone number",
                        },
                        "email": {
                            "type": "string",
                            "description": "The customer's email",
                        },
                        "address": {
                            "type": "string",
                            "description": "The customer's street address",
                        },
                        "birthdate": {
                            "type": "string",
                            "description": "The customer's birthdate. YYYY-MM-DD",
                        },
                        "loyalty_points": {
                            "type": "integer",
                            "description": "The number of loyalty points the customer has",
                        },
                        "memebership_level": {
                            "type": "string",
                            "description": "The membership tier of the customer",
                        },
                        "opt_in_marketing": {
                            "type": "boolean",
                            "description": "OPTIONAL. If the customer is opting into marketing",
                        },
                    },
                },
            },
        }
