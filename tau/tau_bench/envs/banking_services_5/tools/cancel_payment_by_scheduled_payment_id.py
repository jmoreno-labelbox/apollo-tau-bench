# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CancelPaymentByScheduledPaymentId(Tool):
    """Cancels a scheduled payment by updating its status to 'Cancelled' using the scheduled_payment_id,
       and ensures it belongs to the given customer."""

    @staticmethod
    def invoke(data: Dict[str, Any], customer_id = "", scheduled_payment_id = "") -> str:
        customer_id = customer_id.strip()
        scheduled_payment_id = scheduled_payment_id.strip()

        # Check input values for correctness.
        missing = []
        if not customer_id:
            missing.append("customer_id")
        if not scheduled_payment_id:
            missing.append("scheduled_payment_id")
        if missing:
            return json.dumps(
                {"error": f"Missing required fields: {', '.join(missing)}"},
                indent=2
            )

        # Locate and terminate the payment.
        scheduled_payments = data.get("scheduled_payments", [])
        for payment in scheduled_payments:
            if (payment.get("payment_id") == scheduled_payment_id and
                    payment.get("customer_id") == customer_id):
                payment["status"] = "Cancelled"
                return json.dumps({
                    "message": "Scheduled payment cancelled successfully.",
                    "customer_id": customer_id,
                    "payment_id": scheduled_payment_id,
                    "status": "Cancelled"
                }, indent=2)

        return json.dumps({
            "error": "Scheduled payment not found for the given ID and customer."
        }, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "cancel_payment_by_scheduled_payment_id",
                "description": "Cancels a scheduled payment by setting its status to 'Cancelled', verifying customer ownership.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_id": {
                            "type": "string",
                            "description": "ID of the customer who owns the scheduled payment"
                        },
                        "scheduled_payment_id": {
                            "type": "string",
                            "description": "ID of the scheduled payment to cancel"
                        }
                    },
                    "required": ["customer_id", "scheduled_payment_id"]
                }
            }
        }
