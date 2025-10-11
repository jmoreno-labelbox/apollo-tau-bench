# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool




def _ok(**payload) -> str:
    out = {"status": "success"}
    out.update(payload)
    return json.dumps(out)

class CaV2CalculateYtdRevenue(Tool):
    """Calculate year-to-date revenue and tax reserve."""

    @staticmethod
    def invoke(data: Dict[str, Any], tax_rate = 0.265, year = "2024") -> str:

        invoices = data.get("invoices", [])
        ytd_invoices = [inv for inv in invoices
                       if inv.get("invoice_date", "").startswith(year)]

        total_revenue = sum(inv.get("subtotal", 0) for inv in ytd_invoices)
        tax_reserve = round(total_revenue * tax_rate, 2)

        revenue_by_month = {}
        for invoice in ytd_invoices:
            month = invoice.get("invoice_date", "")[:7]  # Year and month format.
            if month not in revenue_by_month:
                revenue_by_month[month] = 0
            revenue_by_month[month] += invoice.get("subtotal", 0)

        return _ok(
            year=year,
            ytd_revenue=total_revenue,
            ytd_tax_reserve=tax_reserve,
            revenue_by_month=revenue_by_month,
            invoice_count=len(ytd_invoices)
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ca_v2_calculate_ytd_revenue",
                "description": "Calculate year-to-date revenue, tax reserve, and monthly breakdown.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "year": {"type": "string"},
                        "tax_rate": {"type": "number", "default": 0.265}
                    },
                    "required": [],
                },
            },
        }