from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class AppendMonthlyRevenueRows(Tool):
    """Add monthly revenue entries for a snapshot."""

    @staticmethod
    def invoke(data: dict[str, Any], snapshot_id: str = None, items: list[dict[str, Any]] = None) -> str:
        rows_tbl = data.get("monthly_revenue", [])
        items = items or []
        inserted = []

        max_id = 0
        for r in rows_tbl:
            try:
                max_id = max(max_id, int(r.get("row_id", 0)))
            except (ValueError, TypeError):
                pass

        for it in items:
            max_id += 1
            rows_tbl.append(
                {
                    "row_id": max_id,
                    "snapshot_id": snapshot_id,
                    "month_year": it.get("month_year"),
                    "revenue": it.get("revenue"),
                    "tax_reserve": it.get("tax_reserve"),
                    "profit_flag": it.get("profit_flag"),
                }
            )
            inserted.append(max_id)
        payload = {"snapshot_id": snapshot_id, "inserted_row_ids": inserted}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "appendMonthlyRevenueRows",
                "description": "Monthly revenue items.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "snapshot_id": {"type": "string"},
                        "items": {"type": "array", "items": {"type": "object"}},
                    },
                    "required": ["snapshot_id", "items"],
                },
            },
        }
