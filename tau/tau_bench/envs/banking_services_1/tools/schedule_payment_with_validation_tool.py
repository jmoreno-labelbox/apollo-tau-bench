# Copyright © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class SchedulePaymentWithValidationTool(Tool):
    """
    Tool for scheduling a future payment with validation of sender's balance.

    This tool ensures that the source account exists and has sufficient funds
    before generating a scheduled payment with a unique payment ID.

    Methods:
        invoke(data: Dict[str, Any], **kwargs) -> str:
            Schedules a payment if the balance is adequate.

        get_info() -> Dict[str, Any]:
            Describes the tool's interface, accepted parameters, and behavior.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], amount, currency, date, from_account, to_account) -> str:

        if not all([from_account, to_account, amount, currency, date]):
            return json.dumps({"error": "Missing required fields"}, indent=2)

        accounts = list(data.get("accounts", {}).values())
        from_acc = next((a for a in accounts if a["account_id"] == from_account), None)
        if not from_acc or from_acc["balance"] < amount:
            return json.dumps(
                {"error": "Insufficient balance or account not found"}, indent=2
            )

        payment_id = f"sched_{generate_unique_id()}"
        return json.dumps(
            {
                "payment_id": payment_id,
                "status": "Scheduled",
                "from": from_account,
                "to": to_account,
                "amount": amount,
                "currency": currency,
                "date": date,
            },
            indent=2,
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "schedule_payment_with_validation",
                "description": "Schedule a payment for a future date with balance validation.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "from_account": {
                            "type": "string",
                            "description": "From account",
                        },
                        "to_account": {"type": "string", "description": "To account"},
                        "amount": {"type": "number", "description": "Amount"},
                        "currency": {"type": "string", "description": "Currency"},
                        "date": {"type": "string", "description": "Date"},
                    },
                    "required": [
                        "from_account",
                        "to_account",
                        "amount",
                        "currency",
                        "date",
                    ],
                },
            },
        }
