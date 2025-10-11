# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class AddNewCustomer(Tool):
    """Creates a new customer profile accepting only essential fields."""

    @staticmethod
    def invoke(data: Dict[str, Any], annual_income, city, country, date_of_birth, email_address, first_name, last_name, phone_number, postal_code, state, street_address) -> str:
        # Necessary inputs
        required = [
            "first_name", "last_name", "date_of_birth", "email_address",
            "phone_number", "street_address", "city","state", "postal_code", "country", "annual_income"
        ]
        missing = [f for f in required if not kwargs.get(f)]
        if missing:
            return json.dumps({"error": f"Missing required fields: {', '.join(missing)}"}, indent=2)

        # Create basic customer profile.
        customer_id = get_next_customer_id()
        date_joined = get_current_timestamp()

        personal_info = {
            "first_name":    first_name,
            "last_name":     last_name,
            "date_of_birth": date_of_birth,
            "annual_income": annual_income
        }
        contact_info = {
            "email_address": email_address,
            "phone_numbers": [{"type": "Mobile", "number": phone_number, "is_primary": True}],
            "mailing_address": {
                "street_address": street_address,
                "city":           city,
                "state":          state,
                "postal_code":    postal_code,
                "country":        country
            },
            "residential_address": {}
        }

        new_customer = {
            "customer_id":       customer_id,
            "personal_info":     personal_info,
            "contact_info":      contact_info,
            "account_ids":       [],
            "bank_relationship": {"date_joined": date_joined, "customer_segment": "Retail"},
            "financial_profile": {"annual_income": annual_income}
        }

        data.setdefault("customers", []).append(new_customer)
        return json.dumps(new_customer, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "add_new_customer",
                "description": "Creates a new customer with only essential profile fields.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "first_name":       {"type": "string"},
                        "last_name":        {"type": "string"},
                        "date_of_birth":    {"type": "string"},
                        "email_address":    {"type": "string"},
                        "phone_number":     {"type": "string"},
                        "street_address":   {"type": "string"},
                        "state":            {"type": "string"},
                        "city":             {"type": "string"},
                        "postal_code":      {"type": "string"},
                        "country":          {"type": "string"},
                        "annual_income":    {"type": "integer"}
                    },
                    "required": [
                        "first_name", "last_name", "date_of_birth", "email_address",
                        "phone_number", "street_address", "city", "state", "postal_code", "country", "annual_income"
                    ]
                }
            }
        }
