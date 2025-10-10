# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CancelScheduledPaymentTool(Tool):
    """
    Tool to cancel a scheduled payment by updating its status to 'Cancelled'.

    This tool locates the scheduled payment by ID and ensures it is in an
    'Active' or 'Scheduled' state before marking it as cancelled and persisting
    the change.

    Methods:
        invoke(data: Dict[str, Any], **kwargs) -> str:
            Cancels the payment if valid and not yet processed.

        get_info() -> Dict[str, Any]:
            Returns metadata for schema validation and integration handling.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], payment_id) -> str:
        if not payment_id:
            return json.dumps({"error": "payment_id is required"}, indent=2)
        payments = load_json("scheduled_payments.json")
        for p in payments:
            if p["payment_id"] == payment_id:
                p["status"] = "Cancelled"
                p["cancelled_at"] = get_current_timestamp()
                return json.dumps(
                    {"status": "Cancelled", "cancelled_at": p["cancelled_at"]}, indent=2
                )
        return json.dumps({"error": "Payment not found"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "cancel_scheduled_payment",
                "description": "Cancel a scheduled payment before execution and refund if necessary.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "payment_id": {
                            "type": "string",
                            "description": "Scheduled payment identifier",
                        }
                    },
                    "required": ["payment_id"],
                },
            },
        }
