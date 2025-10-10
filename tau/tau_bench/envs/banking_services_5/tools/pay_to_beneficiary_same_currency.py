# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class PayToBeneficiarySameCurrency(Tool):
    """Debits a source account and pays a beneficiary in the same currency for a given customer."""

    @staticmethod
    def invoke(data: Dict[str, Any], amount, beneficiary_id, currency, customer_id, source_account_id) -> str:

        if not all([customer_id, beneficiary_id, source_account_id, amount, currency]):
            return json.dumps(
                {"error": "customer_id, beneficiary_id, source_account_id, amount, and currency are required."},
                indent=2
            )

        # Retrieve beneficiary information and confirm ownership.
        ben = next(
            (b for b in list(data.get("beneficiaries", {}).values())
             if b.get("beneficiary_id") == beneficiary_id and b.get("customer_id") == customer_id),
            None
        )
        if not ben:
            return json.dumps({"error": f"Beneficiary '{beneficiary_id}' not found for customer '{customer_id}'."}, indent=2)

        # Retrieve the source account and confirm ownership.
        acct = next(
            (a for a in list(data.get("accounts", {}).values())
             if a.get("account_id") == source_account_id and a.get("customer_id") == customer_id),
            None
        )
        if not acct:
            return json.dumps({"error": f"Source account '{source_account_id}' not found for customer '{customer_id}'."}, indent=2)

        # Validate currency
        if acct.get("currency") != currency:
            return json.dumps(
                {"error": "Currency mismatch for same‑currency payment."},
                indent=2
            )

        # Verify balance
        if acct.get("balance", 0.0) < amount:
            return json.dumps({"error": "Insufficient balance in source account."}, indent=2)

        # Execute debit transaction.
        acct["balance"] -= amount
        target_acc_num = ben["account_details"].get("account_number")

        return json.dumps({
            "message": f"Paid {amount:.2f} {currency} to beneficiary '{ben['beneficiary_name']}' (acct {target_acc_num}).",
            "customer_id": customer_id,
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
                "name": "pay_to_beneficiary_same_currency",
                "description": "Pays a beneficiary in the same currency by debiting the source account for the given customer.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_id": {
                            "type": "string",
                            "description": "ID of the customer performing the payment"
                        },
                        "beneficiary_id": {
                            "type": "string",
                            "description": "ID of the beneficiary to pay"
                        },
                        "source_account_id": {
                            "type": "string",
                            "description": "Account ID to debit"
                        },
                        "amount": {
                            "type": "number",
                            "description": "Amount to pay"
                        },
                        "currency": {
                            "type": "string",
                            "description": "Currency code (must match source account)"
                        }
                    },
                    "required": ["customer_id", "beneficiary_id", "source_account_id", "amount", "currency"]
                }
            }
        }
