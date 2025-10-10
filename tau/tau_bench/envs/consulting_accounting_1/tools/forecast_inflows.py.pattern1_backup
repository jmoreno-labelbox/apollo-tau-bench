# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ForecastInflows(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        invoices_ids = kwargs.get("invoices", [])
        prob_rule = kwargs.get("probability_rule", "overdue_60=0.3")
        discount = 0.3
        try:
            if "overdue_60=" in prob_rule:
                discount = float(prob_rule.split("overdue_60=")[1])
        except Exception:
            discount = 0.3
        import datetime as _dt
        today = _dt.datetime.fromisoformat("2024-11-30")
        invoices = data.get("invoices", [])
        total_expected = 0.0
        breakdown = []
        for inv_id in invoices_ids:
            inv = next((i for i in invoices if i.get("invoice_id") == inv_id), None)
            if not inv or inv.get("paid_at"):
                continue
            inv_date = _dt.datetime.fromisoformat(inv["invoice_date"])
            days = (today - inv_date).days
            amt = float(inv.get("total_due", 0.0))
            prob = discount if days > 60 else 1.0
            expected = round(amt * prob, 2)
            total_expected += expected
            breakdown.append({"invoice_id": inv_id,"days_overdue": days,"amount": amt,"probability": prob,"expected": expected})
        return json.dumps({"total_expected_inflows": round(total_expected, 2),"breakdown": breakdown}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function","function": {"name": "forecast_inflows","description": "Forecast expected inflows from invoices (discount >60d overdue).","parameters": {"type": "object","properties": {"invoices": {"type": "array","items": {"type": "string"}},"probability_rule": {"type": "string"}},"required": ["invoices"]}}}
