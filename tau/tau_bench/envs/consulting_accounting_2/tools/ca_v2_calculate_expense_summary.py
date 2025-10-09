from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta
from typing import Any

class CaV2CalculateExpenseSummary(Tool):
    """Compute a summary of expenses by category for a specified timeframe."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        year: str = "2024",
        start_date: str = None,
        end_date: str = None,
        category_filter: list = None
    ) -> str:
        if category_filter is None:
            category_filter = []

        expenses = data.get("expenses", [])
        expense_categories = data.get("expense_categories", [])

        # Narrow down expenses by date range
        if start_date and end_date:
            filtered_expenses = [
                exp
                for exp in expenses
                if start_date <= exp.get("expense_date", "") <= end_date
            ]
        else:
            # Narrow down expenses by year
            filtered_expenses = [
                exp for exp in expenses if exp.get("expense_date", "").startswith(year)
            ]

        # Narrow down by categories if provided
        if category_filter:
            filtered_expenses = [
                exp
                for exp in filtered_expenses
                if exp.get("category_code") in category_filter
            ]

        # Categorize by group
        category_summary = {}
        for expense in filtered_expenses:
            category_code = expense.get("category_code")
            if category_code not in category_summary:
                category_summary[category_code] = {
                    "total_gross": 0,
                    "total_deductible": 0,
                    "count": 0,
                }

            gross_amount = expense.get("gross_amount", 0)
            allowed_amount = expense.get("allowed_amount", 0)

            category_summary[category_code]["total_gross"] += gross_amount
            category_summary[category_code]["total_deductible"] += allowed_amount
            category_summary[category_code]["count"] += 1

        # Include category names and verify deductible does not surpass gross
        for category_code, summary in category_summary.items():
            category_info = _find_one(
                expense_categories, "category_code", category_code
            )
            summary["category_name"] = (
                category_info.get("name", "Unknown") if category_info else "Unknown"
            )
            summary["deductible_percent"] = (
                category_info.get("deductible_percent", 0) if category_info else 0
            )

            # Confirm deductible remains below gross amount
            if summary["total_deductible"] > summary["total_gross"]:
                summary["total_deductible"] = summary["total_gross"]

        total_deductible = sum(
            summary["total_deductible"] for summary in category_summary.values()
        )

        return _ok(
            year=year,
            category_summary=category_summary,
            total_deductible_expenses=round(total_deductible, 2),
            total_expense_count=len(filtered_expenses),
        )

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CaV2CalculateExpenseSummary",
                "description": "Calculate expense summary by category for a given year.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "year": {"type": "string"},
                        "start_date": {"type": "string", "format": "date"},
                        "end_date": {"type": "string", "format": "date"},
                        "category_filter": {
                            "type": "array",
                            "items": {"type": "string"},
                        },
                    },
                    "required": [],
                },
            },
        }
