# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class AggregateMonthlyExpensesTool(Tool):
    """
    Tool that calculates the total monthly expenses for a customer account.

    It fetches all transactions for a given account and aggregates the
    negative amounts grouped by transaction type (used as a category),
    returning the summarized expenditure per month.

    Methods:
        invoke(data: Dict[str, Any], **kwargs) -> str:
            Executes the logic to aggregate expenses per month.

        get_info() -> Dict[str, Any]:
            Returns metadata including expected input (account_id, month) and output format (monthly totals).
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        account_id = kwargs.get("account_id")
        month = kwargs.get("month")
        if not account_id or not month:
            return json.dumps(
                {
                    "status": "error",
                    "message": "Missing required parameters: 'account_id' and/or 'month'.",
                    "required": ["account_id", "month"],
                },
                indent=2,
            )

        transactions = load_json("transactions.json")
        filtered = [
            t
            for t in transactions
            if t["account_id"] == account_id and t["transaction_date"].startswith(month)
        ]

        categories = {}
        total = 0.0
        for t in filtered:
            cat = t.get("transaction_type", "Uncategorized")
            amount = t.get("amount", 0)
            if amount < 0:
                categories[cat] = categories.get(cat, 0) + amount
                total += amount

        return json.dumps(
            {
                "status": "success",
                "account_id": account_id,
                "month": month,
                "categories": categories,
                "total_spent": total,
            },
            indent=2,
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "aggregate_monthly_expenses",
                "description": "Summarize monthly expenses from transaction history by category (transaction type).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "account_id": {"type": "string", "description": "Account ID"},
                        "month": {
                            "type": "string",
                            "description": "Month in YYYY-MM format (e.g., '2024-06')",
                        },
                    },
                    "required": ["account_id", "month"],
                },
            },
        }
