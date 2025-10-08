from tau_bench.envs.tool import Tool
import json
from datetime import date, datetime, time, timedelta, timezone
from typing import Any, Dict, List

class GetScheduledPaymentDetails(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], payment_id: str = None) -> str:
        payment = next((p for p in data['scheduled_payments'] if p['payment_id'] == payment_id), None)
        if payment:
            return json.dumps(payment)
        return json.dumps({"error": "Scheduled payment not found."})
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "GetScheduledPaymentDetails",
                        "description": "Retrieves the full details of a single scheduled payment.",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "payment_id": {"type": "string"}
                                },
                                "required": ["payment_id"]
                        }
                }
        }
