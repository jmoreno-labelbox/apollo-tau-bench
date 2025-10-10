# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class RetrieveScheduledPaymentsTool(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        customer_id = kwargs.get('customer_id')
        source_account_id = kwargs.get('source_account_id')
        month = kwargs.get('month')
        frequency = kwargs.get('frequency', None)

        scheduled_payments = data.get('scheduled_payments', [])
        results = []

        for payment in scheduled_payments:
            if payment.get('customer_id') != customer_id:
                continue
            if payment.get('from_account_id', None) != source_account_id:
                continue
            next_payment_date = payment.get('next_payment_date', '')
            if not next_payment_date.startswith(month):
                continue
            if frequency and payment.get('frequency') not in frequency:
                continue
            results.append({
                "payment_id": payment.get("payment_id"),
                "amount": payment.get("amount"),
                "frequency": payment.get("frequency"),
                "next_payment_date": payment.get("next_payment_date"),
                "status": payment.get("status"),
                "beneficiary_id": payment.get("beneficiary_id"),
                "from_account_id": payment.get("from_account_id", "N/A"),
            })

        return json.dumps(results, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "retrieve_scheduled_payments",
                "description": "Retrieve scheduled payments for a customer and account, with optional month and frequency filters.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_id": {"type": "string", "description": "Customer identifier"},
                        "source_account_id": {"type": "string", "description": "Source account identifier"},
                        "month": {"type": "string", "description": "Filter payments scheduled for this month (YYYY-MM)"},
                        "frequency": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Filter by frequency (e.g. Monthly, Weekly)"
                        }
                    },
                    "required": ["customer_id", "source_account_id", "month"]
                }
            }
        }
