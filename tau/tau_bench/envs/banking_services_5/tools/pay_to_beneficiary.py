# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class PayToBeneficiary(Tool):
    """Transfers funds from a source account to a beneficiary’s external account."""

    @staticmethod
    def invoke(data: Dict[str, Any], amount, beneficiary_id, currency, source_account_id) -> str:

        # check input values
        missing = [p for p in ("beneficiary_id", "source_account_id", "amount", "currency")
                   if not kwargs.get(p)]
        if missing:
            return json.dumps(
                {"error": f"Missing required fields: {', '.join(missing)}"},
                indent=2
            )

        # identify recipient
        bene = next((b for b in list(data.get("beneficiaries", {}).values())
                     if b["beneficiary_id"] == beneficiary_id), None)
        if not bene:
            return json.dumps(
                {"error": f"Beneficiary '{beneficiary_id}' not found."},
                indent=2
            )

        # locate source account
        acct = next((a for a in list(data.get("accounts", {}).values())
                     if a["account_id"] == source_account_id), None)
        if not acct:
            return json.dumps(
                {"error": f"Source account '{source_account_id}' not found."},
                indent=2
            )


        # verify balance
        if acct.get("balance", 0.0) < amount:
            return json.dumps(
                {"error": "Insufficient balance in source account."},
                indent=2
            )

        # execute debit operation
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
                "name": "pay_to_beneficiary",
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
