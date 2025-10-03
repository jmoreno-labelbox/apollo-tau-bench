from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any, Dict
from datetime import timedelta

class UpdatePaymentBehavior(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], publisher_id: str, avg_days_to_pay: int = None, late_payment_frequency: int = None) -> str:
        """
        Updates or inserts a payment behavior record for a publisher.
        """
        record = next((pb for pb in data["payment_behavior"] if pb["publisher_id"] == publisher_id), None)

        if record:
            if avg_days_to_pay is not None:
                record["avg_days_to_pay"] = avg_days_to_pay
            if late_payment_frequency is not None:
                record["late_payment_frequency"] = late_payment_frequency
            record["last_updated"] = datetime.now().isoformat()
            return json.dumps(record["behavior_id"])

        return json.dumps({"error": f"No payment behavior profile found for publisher {publisher_id}"})
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function", "function": {
                "name": "UpdatePaymentBehavior",
                "description": "Updates the payment behavior data (e.g., avg_days_to_pay) for a given publisher.",
                "parameters": {
                    "type": "object", "properties": {
                        "publisher_id": {"type": "string", "description": "The ID of the publisher to update."},
                        "avg_days_to_pay": {"type": "number", "description": "The new calculated average days to pay."},
                        "late_payment_frequency": {"type": "number",
                                                   "description": "The new calculated late payment frequency (as a decimal)."}
                    },
                    "required": ["publisher_id"],
                },
            },
        }
