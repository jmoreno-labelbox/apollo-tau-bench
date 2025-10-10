# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class find_customers(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        customers = list(data.get("customers", {}).values())

        # If customer id is sent, then it will override all other criteria
        customer_id = kwargs.get("customer_id")

        # These columns will be matched exactly to the value sent
        exact_match_cols = [
            "phone_number",
            "membership_level",
            "birthdate",
            "opt_in_marketing",
            "status",
        ]
        exact_match_values = {k: kwargs.get(k) for k in exact_match_cols}

        # These columns will be matched as long as the database field contains the sent value
        approximate_match_cols = ["name", "email", "address"]
        approximate_match_values = {k: kwargs.get(k) for k in approximate_match_cols}

        # These columns have special matching criteria
        special_match_values = {
            "birth_month": kwargs.get("birth_month"),
            "city": kwargs.get("city"),
        }

        matches = []
        for customer in customers:
            # customer_id takes priority
            if (customer_id is not None) and (customer["customer_id"] == customer_id):
                return json.dumps(customer, indent=2)

            # If all sent criteria match, then add it to the return list
            elif (
                all(
                    [
                        exact_match_values[k] == customer[k]
                        for k in exact_match_values.keys()
                        if exact_match_values[k] is not None
                    ]
                )
                and all(
                    [
                        approximate_match_values[k].lower() in customer[k].lower()
                        for k in approximate_match_values.keys()
                        if approximate_match_values[k] is not None
                    ]
                )
                and all(
                    [
                        (
                            "-{}-".format(special_match_values["birth_month"])
                            in customer["birthdate"]
                        )
                        if special_match_values["birth_month"] is not None
                        else True,
                        (
                            special_match_values["city"].lower()
                            == customer["address"].split(",")[1].strip().lower()
                        )
                        if special_match_values["city"] is not None
                        else True,
                    ]
                )
            ):
                matches.append(customer)

        return json.dumps(matches, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "find_customers",
                "description": "Finds customer matching the sent criteria. Returns an empty list if there are none",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_id": {
                            "type": "string",
                            "description": "The id of the customer to return. If found, the function will return only the customer matching the customer_id",
                        },
                        "phone_number": {
                            "type": "string",
                            "description": "phone number of the customer. Will do an exact match",
                        },
                        "membership_level": {
                            "type": "string",
                            "description": "membership level of the customer. Will do an exact match",
                        },
                        "status": {
                            "type": "string",
                            "description": "status of the customer. Will do an exact match",
                        },
                        "birthdate": {
                            "type": "string",
                            "description": "birth date of the customer. Will do an exact match",
                        },
                        "opt_in_marketing": {
                            "type": "bool",
                            "description": "opt in marketing of the customer. Will do an exact match",
                        },
                        "name": {
                            "type": "string",
                            "description": "name of the customer. Will do an approximate match",
                        },
                        "email": {
                            "type": "string",
                            "description": "email of the customer. Will do an approximate match",
                        },
                        "address": {
                            "type": "string",
                            "description": "address of the customer. Will do an approximate match",
                        },
                        "birth_month": {
                            "type": "integer",
                            "description": "The month the person was born in. Will ignore year and day when matching to birth month",
                        },
                        "city": {
                            "type": "string",
                            "description": "The city the person lives in. Will ignore other values in the address and only focus on the city",
                        },
                    },
                },
            },
        }
