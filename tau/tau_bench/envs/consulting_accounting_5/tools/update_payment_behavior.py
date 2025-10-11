# Copyright Sierra

from datetime import datetime
import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdatePaymentBehavior(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], avg_days_to_pay, late_payment_frequency, publisher_id) -> str:
        """
        Updates or inserts a payment behavior record for a publisher.
        """
        # Ensure payment_behavior is a list before iterating
        payment_behavior = data.get("payment_behavior", [])
        if isinstance(payment_behavior, str):
            # If it's a string, try to parse it as JSON or treat as empty list
            try:
                payment_behavior = json.loads(payment_behavior) if payment_behavior else []
            except (json.JSONDecodeError, TypeError):
                payment_behavior = []
        elif isinstance(payment_behavior, dict):
            # If it's a dict, convert to list of values
            payment_behavior = list(payment_behavior.values())
        elif not isinstance(payment_behavior, list):
            payment_behavior = []
            
        record = next((pb for pb in payment_behavior if pb.get("publisher_id") == publisher_id), None)

        if record:
            if "avg_days_to_pay" in kwargs:
                record["avg_days_to_pay"] = avg_days_to_pay
            if "late_payment_frequency" in kwargs:
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
