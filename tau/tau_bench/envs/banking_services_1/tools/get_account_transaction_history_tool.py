# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetAccountTransactionHistoryTool(Tool):
    """
    Tool to retrieve a list of recent transactions for a specific account.

    This tool returns transaction records including date, amount, type, status,
    and merchant information. It supports optional filtering by date range or type.

    Methods:
        invoke(data: Dict[str, Any], **kwargs) -> str:
            Returns the transaction history of the given account ID.

        get_info() -> Dict[str, Any]:
            Returns metadata for usage context, including expected fields.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], account_id, days = 30) -> str:
        if not account_id:
            return json.dumps({"error": "account_id is required"}, indent=2)

        transactions = load_json("transactions.json")
        current_time = get_current_timestamp()
        cutoff = datetime.strptime(current_time, "%Y-%m-%dT%H:%M:%S.%f") - timedelta(days=days)

        filtered = []
        for t in transactions:
            if t["account_id"] != account_id:
                continue
            try:
                txn_date = datetime.strptime(t["transaction_date"], "%Y-%m-%d")
            except ValueError:
                txn_date = datetime.fromisoformat(
                    t["transaction_date"].replace("Z", "+00:00")
                ).replace(tzinfo=None)
            if txn_date >= cutoff:
                filtered.append(t)

        categorized = {}
        for t in filtered:
            cat = t.get("category", "Uncategorized")
            categorized[cat] = categorized.get(cat, 0) + t.get("amount", 0)

        return json.dumps(
            {"transactions": filtered, "categorized_totals": categorized}, indent=2
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_account_transaction_history",
                "description": "Retrieve and categorize past transactions for the customer's account.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "account_id": {"type": "string", "description": "Account ID"},
                        "days": {
                            "type": "integer",
                            "description": "Number of days to include",
                        },
                    },
                    "required": ["account_id"],
                },
            },
        }
