# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateScheduledPaymentStatus(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        payment_id = kwargs.get("payment_id")
        new_status = kwargs.get("new_status")

        payment = next((p for p in data['scheduled_payments'] if p['payment_id'] == payment_id), None)
        if not payment:
            return json.dumps({"error": "Scheduled payment not found."})

        payment['status'] = new_status
        return json.dumps(payment)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "update_scheduled_payment_status",
                        "description": "Updates the status of a scheduled payment (e.g., Active, Paused, Cancelled).",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "payment_id": {"type": "string"},
                                        "new_status": {"type": "string"}
                                },
                                "required": ["payment_id", "new_status"]
                        }
                }
        }
