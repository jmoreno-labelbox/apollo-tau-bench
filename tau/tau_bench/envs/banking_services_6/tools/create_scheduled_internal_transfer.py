# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateScheduledInternalTransfer(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        payment_id = _get_next_scheduled_payment_id(data)
        customer_id = kwargs.get("customer_id")
        source_account_id = kwargs.get("source_account_id")
        destination_account_id = kwargs.get("destination_account_id")
        amount = kwargs.get("amount")
        frequency = kwargs.get("frequency")
        start_date = kwargs.get("start_date")

        source_account = next((a for a in data['accounts'] if a['account_id'] == source_account_id and a['customer_id'] == customer_id), None)
        dest_account = next((a for a in data['accounts'] if a['account_id'] == destination_account_id and a['customer_id'] == customer_id), None)

        if not source_account or not dest_account:
            return json.dumps({"error": "One or both accounts not found or do not belong to the customer."})

        new_payment = {
                "payment_id": payment_id,
                "customer_id": customer_id,
                "source_account_id": source_account_id,
                "beneficiary_id": None,
                "internal_destination_account_id": destination_account_id,
                "amount": amount,
                "currency": source_account['currency'],
                "frequency": frequency,
                "start_date": start_date,
                "next_payment_date": start_date,
                "status": "Active"
        }
        data['scheduled_payments'].append(new_payment)
        return json.dumps(new_payment)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
                "type": "function",
                "function": {
                        "name": "create_scheduled_internal_transfer",
                        "description": "Schedules a new recurring transfer between a customer's own accounts.",
                        "parameters": {
                                "type": "object",
                                "properties": {
                                        "customer_id": {"type": "string"},
                                        "source_account_id": {"type": "string"},
                                        "destination_account_id": {"type": "string"},
                                        "amount": {"type": "number"},
                                        "frequency": {"type": "string"},
                                        "start_date": {"type": "string"}
                                },
                                "required": ["customer_id", "source_account_id", "destination_account_id", "amount", "frequency", "start_date"]
                        }
                }
        }
