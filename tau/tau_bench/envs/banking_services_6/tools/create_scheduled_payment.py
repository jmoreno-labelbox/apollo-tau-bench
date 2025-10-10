# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateScheduledPayment(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        payment_id = _get_next_scheduled_payment_id(data)
        source_account_id = kwargs.get("source_account_id")
        new_payment = {
                "payment_id": payment_id,
                "customer_id": kwargs.get("customer_id"),
                "source_account_id": source_account_id,
                "beneficiary_id": kwargs.get("beneficiary_id"),
                "amount": kwargs.get("amount"),
                "currency": next((a['currency'] for a in data['accounts'] if a['account_id'] == source_account_id), "EUR"),
                "frequency": kwargs.get("frequency"),
                "start_date": kwargs.get("start_date"),
                "next_payment_date": kwargs.get("start_date"),
                "status": "Active"
        }
        data['scheduled_payments'].append(new_payment)
        return json.dumps(new_payment)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "create_scheduled_payment",
                        "description": "Schedules a new recurring payment.",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "customer_id": {"type": "string"}, "source_account_id": {"type": "string"},
                                        "beneficiary_id": {"type": "string"}, "amount": {"type": "number"}, "frequency": {"type": "string"}, "start_date": {"type": "string"}
                                },
                                "required": ["customer_id", "source_account_id", "beneficiary_id", "amount", "frequency", "start_date"]
                        }
                }
        }
