# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class DeriveCollectionKPIs(Tool):
    """Compute collection KPIs (Total Accounts Receivable, avg daily sales, DSO)."""
    @staticmethod
    def invoke(data: Dict[str, Any], window_months = 12) -> str:
        window_months = int(window_months)
        invs = data.get("invoices", []) or []
        total_ar = sum(float(i.get("total_due", 0)) for i in invs if i.get("paid_at") is None)
        avg_daily_sales = round((sum(float(i.get("subtotal", 0)) for i in invs) / max(1, window_months * 30)), 2)
        dso = round((total_ar / max(0.01, avg_daily_sales)), 2)
        return json.dumps({"window_months": window_months,
                           "total_ar": round(total_ar, 2),
                           "avg_daily_sales": avg_daily_sales,
                           "dso": dso}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {
            "name": "derive_collection_kpis",
            "description": "Compute collection KPIs over a window.",
            "parameters": {"type": "object", "properties": {
                "window_months": {"type": "integer"}
            }, "required": []}
        }}
