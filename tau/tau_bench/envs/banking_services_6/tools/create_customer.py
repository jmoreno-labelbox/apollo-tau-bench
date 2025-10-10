# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateCustomer(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        customer_id = _get_next_customer_id(data)
        new_customer = {
                "customer_id": customer_id,
                "personal_info": {"first_name": kwargs.get("first_name"), "last_name": kwargs.get("last_name"), "date_of_birth": kwargs.get("dob")},
                "contact_info": {
                        "email_address": kwargs.get("email"),
                        "phone_numbers": [{"type": "Mobile", "number": kwargs.get("phone"), "is_primary": True}],
                        "mailing_address": {"street_address": kwargs.get("street"), "city": kwargs.get("city"), "postal_code": kwargs.get("postal_code"),
                                            "country": kwargs.get("country")},
                        "residential_address": {"street_address": kwargs.get("street"), "city": kwargs.get("city"), "postal_code": kwargs.get("postal_code"),
                                                "country": kwargs.get("country")}
                },
                "account_ids": [],
                "financial_profile": {"annual_income": kwargs.get("annual_income")},
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
                        "name": "create_customer",
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
