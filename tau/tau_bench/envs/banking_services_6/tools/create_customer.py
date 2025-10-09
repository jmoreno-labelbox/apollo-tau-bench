from tau_bench.envs.tool import Tool
import json
from datetime import date, datetime, time, timedelta, timezone
from typing import Any, Dict, List

class CreateCustomer(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any],
        first_name: str = None,
        last_name: str = None,
        dob: str = None,
        email: str = None,
        phone: str = None,
        street: str = None,
        city: str = None,
        postal_code: str = None,
        country: str = None,
        annual_income: float = None
    ) -> str:
        customer_id = _get_next_customer_id(data)
        new_customer = {
            "customer_id": customer_id,
            "personal_info": {"first_name": first_name, "last_name": last_name, "date_of_birth": dob},
            "contact_info": {
                "email_address": email,
                "phone_numbers": [{"type": "Mobile", "number": phone, "is_primary": True}],
                "mailing_address": {"street_address": street, "city": city, "postal_code": postal_code, "country": country},
                "residential_address": {"street_address": street, "city": city, "postal_code": postal_code, "country": country}
            },
            "account_ids": [],
            "financial_profile": {"annual_income": annual_income},
            "bank_relationship": {"date_joined": NOW.strftime('%Y-%m-%d')},
            "compliance": {"kyc_status": "Verified", "aml_risk_level": "Low"}
        }
        data['customers'].append(new_customer)
        return json.dumps(new_customer)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "CreateCustomer",
                        "description": "Creates a new customer profile.",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "first_name": {"type": "string"}, "last_name": {"type": "string"}, "dob": {"type": "string"},
                                        "email": {"type": "string"}, "phone": {"type": "string"}, "street": {"type": "string"}, "city": {"type": "string"},
                                        "postal_code": {"type": "string"}, "country": {"type": "string"}, "annual_income": {"type": "integer"}
                                },
                                "required": ["first_name", "last_name", "dob", "email", "phone", "street", "city", "postal_code", "country", "annual_income"]
                        }
                }
        }
