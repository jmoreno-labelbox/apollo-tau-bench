# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class create_customer(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        customers = list(data.get("customers", {}).values())

        # Timestamp needs to be sent for database records
        timestamp = kwargs.get("timestamp")

        # These values must be sent
        required_cols = ["name", "phone_number", "email", "address", "birthdate"]

        # These values have defaults if not sent
        optional_cols = ["loyalty_points", "membership_level", "opt_in_marketing"]

        required_values = {k: kwargs.get(k) for k in required_cols}
        optional_values = {
            "loyalty_points": 0,
            "membership_level": "basic",
            "opt_in_marketing": False,
        }
        optional_values.update({k: kwargs[k] for k in optional_cols if k in kwargs})

        # These values are calculated by the function
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

        # Throw an error if any of the required values are missing
        if any([required_values[k] is None for k in required_values.keys()]):
            return json.dumps(
                {
                    "error": "required values not sent: "
                    + ", ".join(
                        [k for k in required_values if required_values[k] is None]
                    )
                },
                indent=2,
            )

        # This is the order that the items appear in the database
        # May not be necessary since dictionaries are unordered, but it can make valiation easier if the items appear in the same order everytime
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

        # Order the items
        row = required_values | optional_values | fill_in
        row_final = OrderedDict()
        for k in col_order:
            row_final[k] = row[k]

        # Add to the database
        customers.append(json.dumps(row_final, indent=2))

        # Return the whole row for reference
        return json.dumps(row_final, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_customer",
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
                            "type": "boolean",
                            "description": "OPTIONAL. If the customer is opting into marketing. This will default to False",
                        },
                    },
                },
            },
        }
