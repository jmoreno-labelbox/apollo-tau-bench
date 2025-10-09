from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetTotalSalesByDate(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], date: str) -> str:
        transactions = data.get("transactions", [])
        total_sales = 0.0
        transaction_count = 0

        for transaction in transactions:
            if transaction.get("timestamp", "").startswith(date):
                total_sales += transaction.get("total_amount", 0.0)
                transaction_count += 1

        sales_info = {
            "date": date,
            "total_sales": total_sales,
            "transaction_count": transaction_count,
        }
        payload = sales_info
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetTotalSalesByDate",
                "description": "Get total sales amount for a specific date.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "date": {
                            "type": "string",
                            "description": "Date in YYYY-MM-DD format.",
                        }
                    },
                    "required": ["date"],
                },
            },
        }
