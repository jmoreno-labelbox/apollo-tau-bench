from tau_bench.envs.tool import Tool
import json
from datetime import date, datetime, time, timedelta, timezone
from typing import Any, Dict, List

class UpdateScheduledPaymentStatus(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], payment_id: str = None, new_status: str = None) -> str:
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
                        "name": "UpdateScheduledPaymentStatus",
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
