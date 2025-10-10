# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateNewSchedulePayment(Tool):
    """Schedules a new payment for a customer with full validation and logic."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        customer_id       = kwargs.get("customer_id")
        source_account_id = kwargs.get("source_account_id")
        beneficiary_id    = kwargs.get("beneficiary_id")
        amount            = kwargs.get("amount")
        currency          = kwargs.get("currency", "")
        frequency         = kwargs.get("frequency", "One-Time").capitalize()
        start_date_str    = kwargs.get("start_date")
        end_date_str      = kwargs.get("end_date")

        # mandatory fields
        if not all([customer_id, source_account_id, beneficiary_id, amount, currency, frequency, start_date_str]):
            return json.dumps({"error": "All required fields must be provided."}, indent=2)

        # process date strings
        try:
            start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
        except ValueError:
            return json.dumps({"error": "start_date must be YYYY-MM-DD."}, indent=2)
        end_date = None
        if end_date_str:
            try:
                end_date = datetime.strptime(end_date_str, "%Y-%m-%d")
            except ValueError:
                return json.dumps({"error": "end_date must be YYYY-MM-DD."}, indent=2)

        # check the source account and its balance
        account = next((a for a in list(data.get("accounts", {}).values()) if a["account_id"] == source_account_id), None)
        if not account:
            return json.dumps({"error": "Source account not found."}, indent=2)
        if account.get("currency") != currency:
            return json.dumps({"error": "Currency mismatch with source account."}, indent=2)

        if account.get("balance", 0.0) < amount:
            status = "Paused"
        else:
            # subtract right away
            account["balance"] -= amount
            status = "One-Time" if frequency == "One-Time" else "Active"

        # calculate next_payment_date
        if frequency == "One-Time":
            next_payment_date = start_date
        elif frequency == "Weekly":
            next_payment_date = start_date + timedelta(weeks=1)
        elif frequency == "Monthly":
            next_payment_date = add_months(start_date, 1)
        elif frequency == "Quarterly":
            next_payment_date = add_months(start_date, 3)
        elif frequency == "Yearly":
            next_payment_date = add_months(start_date, 12)
        else:
            return json.dumps({"error": f"Unsupported frequency '{frequency}'."}, indent=2)

        # verify end_date
        if end_date and next_payment_date.date() > end_date.date():
            status = "Completed"

        payment_id = get_next_payment_id()
        new_payment = {
            "payment_id": payment_id,
            "customer_id": customer_id,
            "source_account_id": source_account_id,
            "beneficiary_id": beneficiary_id,
            "amount": amount,
            "currency": currency,
            "frequency": frequency,
            "start_date": start_date_str,
            "next_payment_date": next_payment_date.strftime("%Y-%m-%d"),
            "end_date": end_date_str,
            "status": status
        }

        data.setdefault("scheduled_payments", []).append(new_payment)

        return json.dumps({
            "message": "Scheduled payment created successfully.",
            "payment_id": payment_id,
            "status": status,
            "next_payment_date": new_payment["next_payment_date"]
        }, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_new_schedule_payment",
                "description": (
                    "Schedules a new payment with logic for frequency, start/end dates, balance check, "
                    "and updates account balances accordingly."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_id": {"type": "string"},
                        "source_account_id": {"type": "string"},
                        "beneficiary_id": {"type": "string"},
                        "amount": {"type": "number"},
                        "currency": {"type": "string"},
                        "frequency": {
                            "type": "string",
                            "enum": ["One-Time", "Weekly", "Monthly", "Quarterly", "Yearly"]
                        },
                        "start_date": {"type": "string"},
                        "end_date": {"type": "string"}
                    },
                    "required": ["customer_id", "source_account_id", "beneficiary_id", "amount", "currency", "frequency", "start_date"]
                }
            }
        }
