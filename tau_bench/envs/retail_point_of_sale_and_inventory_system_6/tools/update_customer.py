from tau_bench.envs.tool import Tool
import json
from collections import OrderedDict, defaultdict
from typing import Any

class update_customer(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        customer_id: str = None,
        timestamp: str = None,
        name: str = None,
        phone_number: str = None,
        email: str = None,
        address: str = None,
        birthdate: str = None,
        membership_level: str = None,
        status: str = None,
        loyalty_points: int = None,
        opt_in_marketing: bool = None
    ) -> str:
        customers = data.get("customers", [])

        # These parameters are essential for updates
        row_id = customer_id
        timestamp = timestamp

        if (row_id is None) or (timestamp is None):
            payload = {"error": "customer_id and timestamp must be sent"}
            out = json.dumps(payload)
            return out

        # These parameters are being submitted for the update
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
        updating_values = {
            "name": name,
            "phone_number": phone_number,
            "email": email,
            "address": address,
            "birthdate": birthdate,
            "membership_level": membership_level,
            "status": status,
            "loyalty_points": loyalty_points,
            "opt_in_marketing": opt_in_marketing,
        }

        for customer in customers:
            if customer["customer_id"] == row_id:
                for col, value in updating_values.items():
                    # Revise any provided values
                    if value is not None:
                        customer[col] = value

                customer["updated_at"] = timestamp
                payload = customer
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": "no matching records found"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateCustomer",
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
                            "type": \"integer\",
                            "description": "The number of loyalty points the customer has",
                        },
                        "memebership_level": {
                            "type": "string",
                            "description": "The membership tier of the customer",
                        },
                        "opt_in_marketing": {
                            "type": "bool",
                            "description": "OPTIONAL. If the customer is opting into marketing",
                        },
                    },
                },
            },
        }
