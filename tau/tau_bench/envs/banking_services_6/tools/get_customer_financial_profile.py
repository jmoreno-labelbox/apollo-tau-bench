from tau_bench.envs.tool import Tool
import json
from datetime import date, datetime, time, timedelta, timezone
from typing import Any, Dict, List

class GetCustomerFinancialProfile(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], customer_id: str = None) -> str:
        customer = next((c for c in data['customers'] if c['customer_id'] == customer_id), None)
        if customer and "financial_profile" in customer:
            return json.dumps(customer['financial_profile'])
        return json.dumps({"error": "Customer or financial profile not found"})
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "GetCustomerFinancialProfile",
                        "description": "Retrieves the financial profile of a customer.",
                        "parameters": {
                                "type": "object",
                                "properties": {"customer_id": {"type": "string"}},
                                "required": ["customer_id"]
                        }
                }
        }
