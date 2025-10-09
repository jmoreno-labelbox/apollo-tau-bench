from tau_bench.envs.tool import Tool
import json
from datetime import date, datetime, time, timedelta, timezone
from typing import Any, Dict, List

class CreateScheduledInternalTransfer(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], customer_id: str = None, source_account_id: str = None, 
               destination_account_id: str = None, amount: float = None, frequency: str = None, 
               start_date: str = None) -> str:
        payment_id = _get_next_scheduled_payment_id(data)

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
                        "name": "CreateScheduledInternalTransfer",
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
