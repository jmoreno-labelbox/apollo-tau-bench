from tau_bench.envs.tool import Tool
import json
from datetime import date, datetime, time, timedelta, timezone
from typing import Any, Dict, List

class CreateScheduledPayment(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any], 
        customer_id: str = None, 
        source_account_id: str = None, 
        beneficiary_id: str = None, 
        amount: float = None, 
        frequency: str = None, 
        start_date: str = None
    ) -> str:
        payment_id = _get_next_scheduled_payment_id(data)
        new_payment = {
                "payment_id": payment_id,
                "customer_id": customer_id,
                "source_account_id": source_account_id,
                "beneficiary_id": beneficiary_id,
                "amount": amount,
                "currency": next((a['currency'] for a in data['accounts'] if a['account_id'] == source_account_id), "EUR"),
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
                        "name": "CreateScheduledPayment",
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
