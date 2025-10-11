# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetScheduledPaymentDetailsByCustomerIdAndBeneficiaryId(Tool):
    """Returns a scheduled payment object using customer ID and beneficiary ID."""

    @staticmethod
    def invoke(data: Dict[str, Any], beneficiary_id = "", customer_id = "") -> str:
        customer_id = customer_id.strip()
        beneficiary_id = beneficiary_id.strip()

        if not customer_id or not beneficiary_id:
            return json.dumps({
                "error": "customer_id and beneficiary_id are required."
            }, indent=2)

        scheduled_payments = data.get("scheduled_payments", [])
        for payment in scheduled_payments:
            if payment.get("customer_id") == customer_id and payment.get("beneficiary_id") == beneficiary_id:
                return json.dumps(payment, indent=2)

        return json.dumps({
            "error": "No scheduled payment found for the given customer and beneficiary."
        }, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_payment_id_by_customer_id_and_beneficiary_id",
                "description": "Returns a scheduled payment using customer ID and beneficiary ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_id": {
                            "type": "string",
                            "description": "ID of the customer"
                        },
                        "beneficiary_id": {
                            "type": "string",
                            "description": "ID of the beneficiary"
                        }
                    },
                    "required": ["customer_id", "beneficiary_id"]
                }
            }
        }
