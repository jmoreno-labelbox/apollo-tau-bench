from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetSalesForCategoryInPeriod(Tool):
    """Fetches sales statistics for a specific category within a date range."""

    @staticmethod
    def invoke(data: dict[str, Any], category: str = None, start_date: str = None, end_date: str = None) -> str:
        sales_data = data.get("f_sales", {}).values()

        matching_sales = []

        for entry in sales_data:
            if (
                entry.get("category") == category
                and entry.get("start_date") >= start_date
                and entry.get("end_date") <= end_date
            ):
                matching_sales.append(entry)
        payload = {"sales_data": matching_sales}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetSalesForCategoryInPeriod",
                "description": "Retrieves sales data for a specific category and date range.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "category": {
                            "type": "string",
                            "description": "The category to analyze.",
                        },
                        "start_date": {
                            "type": "string",
                            "description": "The start date of the period (YYYY-MM-DD format).",
                        },
                        "end_date": {
                            "type": "string",
                            "description": "The end date of the period (YYYY-MM-DD format).",
                        },
                    },
                    "required": ["category", "start_date", "end_date"],
                },
            },
        }
