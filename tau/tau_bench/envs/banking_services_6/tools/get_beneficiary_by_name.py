from tau_bench.envs.tool import Tool
import json
from datetime import date, datetime, time, timedelta, timezone
from typing import Any, Dict, List

class GetBeneficiaryByName(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], customer_id: str = None, beneficiary_name: str = None) -> str:
        beneficiary = next((b for b in data['beneficiaries'] if b['customer_id'] == customer_id and b['beneficiary_name'].lower().strip() == beneficiary_name.lower().strip()),
                           None)
        if beneficiary:
            return json.dumps(beneficiary)
        return json.dumps({"error": "Beneficiary not found"})
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "GetBeneficiaryByName",
                        "description": "Finds a beneficiary for a customer by their name.",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "customer_id": {"type": "string"},
                                        "beneficiary_name": {"type": "string"}
                                },
                                "required": ["customer_id", "beneficiary_name"]
                        }
                }
        }
