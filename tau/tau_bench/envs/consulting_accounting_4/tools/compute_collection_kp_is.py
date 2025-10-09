from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class ComputeCollectionKPIs(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], window_months: int = 12) -> str:
        invs = data.get("invoices", {}).values() or []
        total_ar = sum(
            float(i.get("total_due", 0)) for i in invs.values() if i.get("paid_at") is None
        )
        avg_daily_sales = round(
            (
                sum(float(i.get("subtotal", 0)) for i in invs.values())
                / max(1, window_months * 30)
            ),
            2,
        )
        dso = round((total_ar / max(0.01, avg_daily_sales)), 2)
        payload = {
                "window_months": window_months,
                "total_ar": round(total_ar, 2),
                "avg_daily_sales": avg_daily_sales,
                "dso": dso,
            }
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ComputeCollectionKpis",
                "description": "Compute A/R collection KPIs (total A/R, avg daily sales, DSO) over a window.",
                "parameters": {
                    "type": "object",
                    "properties": {"window_months": {"type": "integer"}},
                    "required": [],
                },
            },
        }
