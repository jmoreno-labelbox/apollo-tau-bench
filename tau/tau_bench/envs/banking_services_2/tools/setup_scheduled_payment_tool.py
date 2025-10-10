# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import generate_unique_id


class SetupScheduledPaymentTool(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        customer_id = kwargs.get('customer_id')
        from_account_id = kwargs.get('from_account_id')
        beneficiary_id = kwargs.get('beneficiary_id')
        amount = kwargs.get('amount')
        frequency = kwargs.get('frequency')
        start_date = kwargs.get('start_date')

        scheduled_payments = data.get('scheduled_payments', [])

        payment_id = f"sched_{generate_unique_id()}"

        new_payment = {
            "payment_id": payment_id,
            "customer_id": customer_id,
            "from_account_id": from_account_id,
            "beneficiary_id": beneficiary_id,
            "amount": amount,
            "frequency": frequency,
            "start_date": start_date,
            "status": "Active",
            "created_date": get_current_timestamp(),
            "next_payment_date": start_date
        }

        scheduled_payments.append(new_payment)

        return json.dumps({
            "payment_id": payment_id,
            "status": "Active",
            "next_payment_date": start_date,
            "amount": amount,
            "frequency": frequency
        }, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "setup_scheduled_payment",
                "description": "Setup a recurring scheduled payment",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_id": {"type": "string", "description": "Customer identifier"},
                        "from_account_id": {"type": "string", "description": "Source account"},
                        "beneficiary_id": {"type": "string", "description": "Beneficiary identifier"},
                        "amount": {"type": "number", "description": "Payment amount"},
                        "frequency": {"type": "string", "description": "Payment frequency", "enum": ["Weekly", "Monthly", "Quarterly"]},
                        "start_date": {"type": "string", "description": "First payment date (YYYY-MM-DD)"}
                    },
                    "required": ["customer_id", "from_account_id", "beneficiary_id", "amount", "frequency", "start_date"]
                }
            }
        }
