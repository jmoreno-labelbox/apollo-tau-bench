# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetScheduledPaymentDetails(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], payment_id) -> str:
        payment = next((p for p in data['scheduled_payments'] if p['payment_id'] == payment_id), None)
        if payment:
            return json.dumps(payment)
        return json.dumps({"error": "Scheduled payment not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "get_scheduled_payment_details",
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
