from tau_bench.envs.tool import Tool
import json
from datetime import date, datetime, time, timedelta, timezone
from typing import Any, Dict, List

class AddBeneficiary(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], customer_id: str = None, name: str = None, relationship: str = None, iban: str = None, account_number: str = None, sort_code: str = None, routing_number: str = None, bank_name: str = None, country: str = None) -> str:
        beneficiary_id = _get_next_beneficiary_id(data)
        new_beneficiary = {
                "beneficiary_id": beneficiary_id,
                "customer_id": customer_id,
                "beneficiary_name": name,
                "relationship": relationship,
                "account_details": {
                        "iban": iban,
                        "account_number": account_number,
                        "sort_code": sort_code,
                        "routing_number": routing_number,
                        "bank_name": bank_name,
                        "country": country
                },
                "date_added": NOW.strftime(DT_STR_FORMAT)
        }
        data['beneficiaries'].append(new_beneficiary)
        return json.dumps(new_beneficiary)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "AddBeneficiary",
                        "description": "Adds a new beneficiary to a customer's profile.",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "customer_id": {"type": "string"}, "name": {"type": "string"}, "relationship": {"type": "string"},
                                        "iban": {"type": "string"},
                                        "account_number": {"type": "string"},
                                        "sort_code": {"type": "string"},
                                        "routing_number": {"type": "string"},
                                        "bank_name": {"type": "string"}, "country": {"type": "string"}
                                },
                                "required": ["customer_id", "name", "relationship", "iban", "bank_name", "country"]
                        }
                }
        }
