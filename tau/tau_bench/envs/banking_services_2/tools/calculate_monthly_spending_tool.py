from tau_bench.envs.tool import Tool
from typing import Any, Dict
import json

class CalculateMonthlySpendingTool(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], account_id: str = None, month: int = None, year: int = None) -> str:
        transactions = data.get('transactions', [])

        total_spending = 0
        spending_by_category = {}
        transaction_count = 0

        for transaction in transactions:
            if transaction['account_id'] != account_id:
                continue
            if transaction['amount'] >= 0:
                continue

            trans_date = transaction['transaction_date']
            if f"{year}-{month:02d}" not in trans_date:
                continue

            amount = abs(transaction['amount'])
            total_spending += amount
            transaction_count += 1

            merchant = transaction.get('merchant_name', 'Other')
            if merchant not in spending_by_category:
                spending_by_category[merchant] = 0
            spending_by_category[merchant] += amount

        return json.dumps({
            "account_id": account_id,
            "month": f"{year}-{month:02d}",
            "total_spending": total_spending,
            "transaction_count": transaction_count,
            "spending_by_merchant": spending_by_category,
            "average_transaction": round(total_spending / max(1, transaction_count), 2)
        }, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CalculateMonthlySpending",
                "description": "Calculate spending summary for a specific month",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "account_id": {"type": "string", "description": "Account identifier"},
                        "month": {"type": "integer", "description": "Month (1-12)"},
                        "year": {"type": "integer", "description": "Year"}
                    },
                    "required": ["account_id", "month", "year"]
                }
            }
        }
