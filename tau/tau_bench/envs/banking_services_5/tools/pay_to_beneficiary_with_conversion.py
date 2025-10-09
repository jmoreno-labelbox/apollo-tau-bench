from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime, timezone, date, timedelta
import calendar
from typing import Any, Dict
import random

class PayToBeneficiaryWithConversion(Tool):

    @staticmethod
    def invoke(
        data: Dict[str, Any], 
        customer_id: str = None, 
        beneficiary_id: str = None, 
        source_account_id: str = None, 
        source_amount: float = None, 
        source_currency: str = None, 
        target_currency: str = None
    ) -> str:
        if not all([customer_id, beneficiary_id, source_account_id, source_amount, source_currency, target_currency]):
            return json.dumps(
                {"error": "customer_id, beneficiary_id, source_account_id, source_amount, source_currency, and target_currency are required."},
                indent=2
            )

        # lookup beneficiary and verify ownership
        ben = next(
            (b for b in data.get("beneficiaries", [])
             if b.get("beneficiary_id") == beneficiary_id and b.get("customer_id") == customer_id),
            None
        )
        if not ben:
            return json.dumps(
                {"error": f"Beneficiary '{beneficiary_id}' not found for customer '{customer_id}'."},
                indent=2
            )

        # lookup source account and verify ownership
        acct = next(
            (a for a in data.get("accounts", [])
             if a.get("account_id") == source_account_id and a.get("customer_id") == customer_id),
            None
        )
        if not acct:
            return json.dumps(
                {"error": f"Source account '{source_account_id}' not found for customer '{customer_id}'."},
                indent=2
            )

        # currency & balance checks
        if acct.get("currency") != source_currency:
            return json.dumps({"error": "Source currency mismatch."}, indent=2)
        if acct.get("balance", 0.0) < source_amount:
            return json.dumps({"error": "Insufficient balance in source account."}, indent=2)

        # determine conversion rate
        rates = {
            "USD_EUR": 0.85,
            "EUR_USD": 1.18,
            "USD_GBP": 0.75,
            "GBP_USD": 1.33,
            "USD_CAD": 1.25,
            "CAD_USD": 0.80,
        }
        key = f"{source_currency.upper()}_{target_currency.upper()}"
        rate = rates.get(key)
        if rate is None:
            return json.dumps(
                {"error": f"No conversion rate for {source_currency} to {target_currency}."},
                indent=2
            )

        target_amount = round(source_amount * rate, 2)

        # debit and pay
        acct["balance"] -= source_amount
        target_acc_num = ben["account_details"].get("account_number")

        return json.dumps({
            "message": f"Paid {target_amount:.2f} {target_currency} to beneficiary '{ben['beneficiary_name']}'.",
            "customer_id": customer_id,
            "source_account_id": source_account_id,
            "beneficiary_account_number": target_acc_num,
            "source_amount": source_amount,
            "source_currency": source_currency,
            "target_amount": target_amount,
            "target_currency": target_currency,
            "new_source_balance": acct["balance"]
        }, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "PayToBeneficiaryWithConversion",
                "description": "Pays a beneficiary in a different currency by debiting the source account for a given customer.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "customer_id":       {"type": "string", "description": "ID of the customer performing the payment"},
                        "beneficiary_id":    {"type": "string", "description": "ID of the beneficiary to pay"},
                        "source_account_id": {"type": "string", "description": "Account ID to debit"},
                        "source_amount":     {"type": "number", "description": "Amount in source currency to debit"},
                        "source_currency":   {"type": "string", "description": "Currency code of the source amount"},
                        "target_currency":   {"type": "string", "description": "Currency code to convert to"}
                    },
                    "required": [
                        "customer_id",
                        "beneficiary_id",
                        "source_account_id",
                        "source_amount",
                        "source_currency",
                        "target_currency"
                    ]
                }
            }
        }
