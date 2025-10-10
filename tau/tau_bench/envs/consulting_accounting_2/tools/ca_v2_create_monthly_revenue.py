# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CaV2CreateMonthlyRevenue(Tool):
    """Create monthly revenue record for dashboard snapshot."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        row_id = kwargs.get("row_id")
        snapshot_id = kwargs.get("snapshot_id")
        month_year = kwargs.get("month_year")
        revenue = kwargs.get("revenue")
        tax_reserve = kwargs.get("tax_reserve")
        profit_flag = kwargs.get("profit_flag", "normal")

        if not all([month_year, revenue, tax_reserve]):
            return _error("Required fields: month_year, revenue, tax_reserve")

        monthly_revenue = {
            "row_id": row_id or f"REV{len(data.get('monthly_revenue', [])) + 1:03d}",
            "snapshot_id": snapshot_id or f"SNAP{len(data.get('dashboard_snapshots', [])) + 1:03d}",
            "month_year": month_year,
            "revenue": revenue,
            "tax_reserve": tax_reserve,
            "profit_flag": profit_flag
        }

        data.setdefault("monthly_revenue", []).append(monthly_revenue)

        return _ok(row_id=monthly_revenue["row_id"], month_year=month_year, revenue=revenue)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ca_v2_create_monthly_revenue",
                "description": "Create a monthly revenue record for a dashboard snapshot.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "row_id": {"type": "string"},
                        "snapshot_id": {"type": "string"},
                        "month_year": {"type": "string"},
                        "revenue": {"type": "number"},
                        "tax_reserve": {"type": "number"},
                        "profit_flag": {"type": "string"}
                    },
                    "required": ["month_year", "revenue", "tax_reserve"],
                },
            },
        }
