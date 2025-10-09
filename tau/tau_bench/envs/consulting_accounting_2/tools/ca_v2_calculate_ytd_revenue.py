from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class CaV2CalculateYtdRevenue(Tool):
    """Compute revenue and tax reserve from the start of the year."""

    @staticmethod
    def invoke(data: dict[str, Any], year: str = "2024", tax_rate: float = 0.265) -> str:
        invoices = data.get("invoices", {}).values()
        ytd_invoices = [
            inv for inv in invoices.values() if inv.get("invoice_date", "").startswith(year)
        ]

        total_revenue = sum(inv.get("subtotal", 0) for inv in ytd_invoices.values()
        tax_reserve = round(total_revenue * tax_rate, 2)

        revenue_by_month = {}
        for invoice in ytd_invoices:
            month = invoice.get("invoice_date", "")[:7]  # Year-Month
            if month not in revenue_by_month:
                revenue_by_month[month] = 0
            revenue_by_month[month] += invoice.get("subtotal", 0)

        return _ok(
            year=year,
            ytd_revenue=total_revenue,
            ytd_tax_reserve=tax_reserve,
            revenue_by_month=revenue_by_month,
            invoice_count=len(ytd_invoices),
        )

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CaV2CalculateYtdRevenue",
                "description": "Calculate year-to-date revenue, tax reserve, and monthly breakdown.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "year": {"type": "string"},
                        "tax_rate": {"type": "number", "default": 0.265},
                    },
                    "required": [],
                },
            },
        }
