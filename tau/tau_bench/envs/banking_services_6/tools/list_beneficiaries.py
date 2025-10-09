from tau_bench.envs.tool import Tool
import json
from datetime import date, datetime, time, timedelta, timezone
from typing import Any, Dict, List

class ListBeneficiaries(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], customer_id: str = None) -> str:
        customer_beneficiaries = [b for b in data['beneficiaries'] if b['customer_id'] == customer_id]
        return json.dumps(customer_beneficiaries)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "ListBeneficiaries",
                        "description": "Lists all beneficiaries for a given customer.",
                        "parameters": {
                                "type": "object",
                                "properties": {"customer_id": {"type": "string"}},
                                "required": ["customer_id"]
                        }
                }
        }
