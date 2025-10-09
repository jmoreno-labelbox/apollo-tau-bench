from tau_bench.envs.tool import Tool
import json
import os
from datetime import datetime, timedelta
from typing import Any, Dict



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

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
    def invoke(
        data: Dict[str, Any],
        from_account: str = None,
        to_account: str = None,
        amount: float = None,
        currency: str = None,
        date: str = None
    ) -> str:
        if not all([from_account, to_account, amount, currency, date]):
            return json.dumps({"error": "Missing required fields"}, indent=2)

        accounts = data.get("accounts", [])
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
        if not all([from_account, to_account, amount, currency, date]):
            return json.dumps({"error": "Missing required fields"}, indent=2)

        accounts = data.get("accounts", [])
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
                "name": "SchedulePaymentWithValidation",
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
