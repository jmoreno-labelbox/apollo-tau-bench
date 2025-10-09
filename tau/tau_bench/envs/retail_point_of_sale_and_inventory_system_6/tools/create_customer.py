from tau_bench.envs.tool import Tool
import json
from collections import OrderedDict, defaultdict
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class create_customer(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        timestamp: str = None,
        name: str = None,
        phone_number: str = None,
        email: str = None,
        address: str = None,
        birthdate: str = None,
        loyalty_points: int = 0,
        membership_level: str = "basic",
        opt_in_marketing: bool = False,
    ) -> str:
        pass
        customers = data.get("customers", [])

        # A timestamp must be included for database entries

        # These values are required to be sent
        required_cols = ["name", "phone_number", "email", "address", "birthdate"]

        # Default values apply if these are not provided
        optional_cols = ["loyalty_points", "membership_level", "opt_in_marketing"]

        required_values = {
            "name": name,
            "phone_number": phone_number,
            "email": email,
            "address": address,
            "birthdate": birthdate,
        }
        optional_values = {
            "loyalty_points": loyalty_points,
            "membership_level": membership_level,
            "opt_in_marketing": opt_in_marketing,
        }

        # The function computes these values
        fill_in = {
            "customer_id": "CUST-5{customer_id:03}".format(
                customer_id=max(
                    [int(x["customer_id"].split("-")[1][1:]) for x in customers]
                )
                + 1
            ),
            "created_at": timestamp,
            "updated_at": timestamp,
            "status": "active",
        }

        # Raise an error if any required values are absent
        if any([required_values[k] is None for k in required_values.keys()]):
            payload = {
                "error": "required values not sent: "
                + ", ".join(
                    [k for k in required_values if required_values[k] is None]
                )
            }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        # This indicates the sequence of items in the database
        # Although not essential due to the unordered nature of dictionaries, maintaining the same order can simplify validation
        col_order = [
            "customer_id",
            "name",
            "phone_number",
            "loyalty_points",
            "email",
            "address",
            "membership_level",
            "birthdate",
            "opt_in_marketing",
            "created_at",
            "updated_at",
            "status",
        ]

        # Arrange the items
        row = required_values | optional_values | fill_in
        row_final = OrderedDict()
        for k in col_order:
            row_final[k] = row[k]

        # Insert into the database
        customers.append(json.dumps(row_final, indent=2))
        payload = row_final
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateCustomer",
                "description": "Creates a new customer record",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "timestamp": {
                            "type": "string",
                            "description": "The current timestamp. Used for database timestamp rows",
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
                            "description": "OPTIONAL. The number of loyalty points the customer has. This will normally be 0, but sometimes they can start with points as an incentive to create an account.",
                        },
                        "memebership_level": {
                            "type": "string",
                            "description": "OPTIONAL. The membership tier the customer is starting on. This will default to 'basic'.",
                        },
                        "opt_in_marketing": {
                            "type": \"boolean\",
                            "description": "OPTIONAL. If the customer is opting into marketing. This will default to False",
                        },
                    },
                },
            },
        }
