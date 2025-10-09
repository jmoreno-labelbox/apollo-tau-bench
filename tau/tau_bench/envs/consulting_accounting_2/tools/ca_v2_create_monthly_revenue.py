from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class CaV2CreateMonthlyRevenue(Tool):
    """Generate a monthly revenue entry for the dashboard snapshot."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        row_id: str = None,
        snapshot_id: str = None,
        month_year: str = None,
        revenue: float = None,
        tax_reserve: float = None,
        profit_flag: str = "normal"
    ) -> str:
        if not all([month_year, revenue, tax_reserve]):
            return _error("Required fields: month_year, revenue, tax_reserve")

        monthly_revenue = {
            "row_id": row_id or f"REV{len(data.get('monthly_revenue', {})) + 1:03d}",
            "snapshot_id": snapshot_id
            or f"SNAP{len(data.get('dashboard_snapshots', {})) + 1:03d}",
            "month_year": month_year,
            "revenue": revenue,
            "tax_reserve": tax_reserve,
            "profit_flag": profit_flag,
        }

        data.setdefault("monthly_revenue", []).append(monthly_revenue)

        return _ok(
            row_id=monthly_revenue["row_id"], month_year=month_year, revenue=revenue
        )

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CaV2CreateMonthlyRevenue",
                "description": "Create a monthly revenue record for a dashboard snapshot.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "row_id": {"type": "string"},
                        "snapshot_id": {"type": "string"},
                        "month_year": {"type": "string"},
                        "revenue": {"type": "number"},
                        "tax_reserve": {"type": "number"},
                        "profit_flag": {"type": "string"},
                    },
                    "required": ["month_year", "revenue", "tax_reserve"],
                },
            },
        }
