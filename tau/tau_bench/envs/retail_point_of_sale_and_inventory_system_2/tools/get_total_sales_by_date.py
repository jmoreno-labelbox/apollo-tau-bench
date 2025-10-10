# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetTotalSalesByDate(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], date: str) -> str:
        transactions = list(data.get("transactions", {}).values())
        total_sales = 0.0
        transaction_count = 0

        for transaction in transactions:
            if transaction.get("timestamp", "").startswith(date):
                total_sales += transaction.get("total_amount", 0.0)
                transaction_count += 1

        sales_info = {
            "date": date,
            "total_sales": total_sales,
            "transaction_count": transaction_count
        }
                return json.dumps(sales_info, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_total_sales_by_date",
                "description": "Get total sales amount for a specific date.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "date": {"type": "string", "description": "Date in YYYY-MM-DD format."}
                    },
                    "required": ["date"]
                }
            }
        }
