from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime, timezone, date, timedelta
import calendar
from typing import Any, Dict
import random

class AddNewCustomer(Tool):

    def invoke(
        data: Dict[str, Any],
        first_name: str,
        annual_income: float = None,
        city: str = None,
        country: str = None,
        date_of_birth: str = None,
        email_address: str = None,
        last_name: str = None,
        phone_number: str = None,
        postal_code: str = None,
        state: str = None,
        street_address: str = None
    ) -> str:
        # Required inputs
        required = [
            "first_name", "last_name", "date_of_birth", "email_address",
            "phone_number", "street_address", "city", "state", "postal_code", "country", "annual_income"
        ]
        params_dict = {k: v for k, v in locals().items() if k != "data"}

        missing = [f for f in required.values() if params_dict.get(f) is None]
        if missing:
            return json.dumps({"error": f"Missing required fields: {', '.join(missing)}"}, indent=2)

        # Build minimal customer record
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
                "name": "addNewCustomer",
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
