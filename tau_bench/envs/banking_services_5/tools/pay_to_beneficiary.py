from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime, timezone, date, timedelta
import calendar
from typing import Any, Dict
import random

class PayToBeneficiary(Tool):

    @staticmethod
    def invoke(data: Dict[str, Any], beneficiary_id: str = None, source_account_id: str = None, amount: float = None, currency: str = None) -> str:
        # validate inputs
        params_dict = {k: v for k, v in locals().items() if k != "data"}
        missing = [p for p in ("beneficiary_id", "source_account_id", "amount", "currency")
                   if params_dict.get(p) is None]
        if missing:
            return json.dumps(
                {"error": f"Missing required fields: {', '.join(missing)}"},
                indent=2
            )

        # find beneficiary
        bene = next((b for b in data.get("beneficiaries", [])
                     if b["beneficiary_id"] == beneficiary_id), None)
        if not bene:
            return json.dumps(
                {"error": f"Beneficiary '{beneficiary_id}' not found."},
                indent=2
            )

        # find source account
        acct = next((a for a in data.get("accounts", [])
                     if a["account_id"] == source_account_id), None)
        if not acct:
            return json.dumps(
                {"error": f"Source account '{source_account_id}' not found."},
                indent=2
            )

        # balance check
        if acct.get("balance", 0.0) < amount:
            return json.dumps(
                {"error": "Insufficient balance in source account."},
                indent=2
            )

        # perform debit
        acct["balance"] -= amount
        target_acc_num = bene["account_details"].get("account_number")

        return json.dumps({
            "message": f"Paid {amount:.2f} {currency} to beneficiary '{bene['beneficiary_name']}' "
                       f"(account {target_acc_num}).",
            "source_account_id": source_account_id,
            "beneficiary_account_number": target_acc_num,
            "amount": amount,
            "currency": currency,
            "new_source_balance": acct["balance"]
        }, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "payToBeneficiary",
                "description": (
                    "Debits the specified amount and currency from a source account and pays it "
                    "to the external account number stored for the given beneficiary."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "beneficiary_id": {
                            "type": "string",
                            "description": "Identifier of the beneficiary to pay"
                        },
                        "source_account_id": {
                            "type": "string",
                            "description": "Account ID from which funds will be debited"
                        },
                        "amount": {
                            "type": "number",
                            "description": "Amount to debit and pay"
                        },
                        "currency": {
                            "type": "string",
                            "description": "Currency of the payment (must match the source account)"
                        }
                    },
                    "required": [
                        "beneficiary_id",
                        "source_account_id",
                        "amount",
                    ]
                }
            }
        }
