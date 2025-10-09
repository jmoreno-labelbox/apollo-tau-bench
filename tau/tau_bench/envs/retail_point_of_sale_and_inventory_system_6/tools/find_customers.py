from tau_bench.envs.tool import Tool
import json
from collections import OrderedDict, defaultdict
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class find_customers(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        customer_id: str = None,
        phone_number: str = None,
        membership_level: str = None,
        birthdate: str = None,
        opt_in_marketing: bool = None,
        status: str = None,
        name: str = None,
        email: str = None,
        address: str = None,
        birth_month: str = None,
        city: str = None,
    ) -> str:
        customers = data.get("customers", {}).values()

        # If a customer id is provided, it will supersede all other criteria

        # These columns will match exactly with the provided value
        exact_match_cols = [
            "phone_number",
            "membership_level",
            "birthdate",
            "opt_in_marketing",
            "status",
        ]
        exact_match_values = {
            "phone_number": phone_number,
            "membership_level": membership_level,
            "birthdate": birthdate,
            "opt_in_marketing": opt_in_marketing,
            "status": status,
        }

        # These columns will match as long as the database field has the provided value
        approximate_match_cols = ["name", "email", "address"]
        approximate_match_values = {
            "name": name,
            "email": email,
            "address": address,
        }

        # These columns have distinct matching criteria
        special_match_values = {
            "birth_month": birth_month,
            "city": city,
        }

        matches = []
        for customer in customers.values():
            # customer_id is given priority
            if (customer_id is not None) and (customer["customer_id"] == customer_id):
                payload = customer
                out = json.dumps(payload, indent=2)
                return out

            # Include in the return list if all provided criteria match
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
                            (
                                "-{}-".format(special_match_values["birth_month"])
                                in customer["birthdate"]
                            )
                            if special_match_values["birth_month"] is not None
                            else True
                        ),
                        (
                            (
                                special_match_values["city"].lower()
                                == customer["address"].split(",")[1].strip().lower()
                            )
                            if special_match_values["city"] is not None
                            else True
                        ),
                    ]
                )
            ):
                matches.append(customer)
        payload = matches
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FindCustomers",
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
                            "type": "boolean",
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
