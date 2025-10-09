from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetAverageDailySalesForCategoryInPeriod(Tool):
    """Computes average daily sales for a category during a date range."""

    @staticmethod
    def invoke(data: dict[str, Any], category: str = None, start_date: str = None, end_date: str = None) -> str:
        sales_data = data.get("f_sales", [])

        # Determine the total days within the timeframe
        start = datetime.strptime(start_date, "%Y-%m-%d")
        end = datetime.strptime(end_date, "%Y-%m-%d")
        days_in_period = (end - start).days + 1

        total_units = 0
        total_revenue = 0

        for entry in sales_data:
            if (
                entry.get("category") == category
                and entry.get("start_date") >= start_date
                and entry.get("end_date") <= end_date
            ):
                total_units += entry.get("units", 0)
                total_revenue += entry.get("revenue", 0)

        # Compute averages
        avg_units = total_units / days_in_period if days_in_period > 0 else 0
        avg_revenue = total_revenue / days_in_period if days_in_period > 0 else 0
        payload = {
            "average_units": avg_units,
            "average_revenue": avg_revenue,
            "days_in_period": days_in_period,
        }
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getAverageDailySalesForCategoryInPeriod",
                "description": "Calculates average daily sales for a category over a date range.",
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
