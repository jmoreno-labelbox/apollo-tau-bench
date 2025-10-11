# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool






class ForecastOutflows(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], recurring_schedules = True, taxes = True, horizon_months = 3) -> str:
        include_sched = bool(recurring_schedules)
        include_taxes = bool(taxes)
        horizon_months = int(horizon_months)
        total = 0.0
        lines: List[Dict[str, Any]] = []
        if include_sched:
            for s in data.get("recurring_schedules", []):
                if not s.get("is_active", False):
                    continue
                freq = s.get("frequency")
                amt = float(s.get("amount", 0.0))
                if freq == "monthly":
                    count = horizon_months
                elif freq == "quarterly":
                    count = max(1, horizon_months // 3)
                elif freq == "annual":
                    count = 1 if horizon_months >= 12 else 0
                elif freq == "one_time":
                    count = 1
                else:
                    count = 1
                total += amt * count
                lines.append({"schedule_id": s.get("schedule_id"),"frequency": freq,"instances": count,"amount_per_instance": amt,"total": round(amt * count, 2)})
        if include_taxes:
            taxes = [s for s in data.get("recurring_schedules", []) if s.get("schedule_type") in ("tax_payment",)]
            for t in taxes:
                amt = float(t.get("amount", 0.0))
                total += amt
                lines.append({"schedule_id": t.get("schedule_id"),"frequency": t.get("frequency"),"instances": 1,"amount_per_instance": amt,"total": amt,"type": "tax"})
        return json.dumps({"total_expected_outflows": round(total, 2),"lines": lines}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function","function": {"name": "forecast_outflows","description": "Forecast expected outflows from recurring schedules and taxes.","parameters": {"type": "object","properties": {"recurring_schedules": {"type": "boolean"},"taxes": {"type": "boolean"},"horizon_months": {"type": "integer"}}}}}

class ForecastInflows(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], invoices = [], probability_rule = "overdue_60=0.3") -> str:
        invoices_ids = invoices
        prob_rule = probability_rule
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

class BuildCashflowView(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], granularity = "monthly", horizon_months = 3) -> str:
        horizon = int(horizon_months)
        gran = granularity
        opening = 0.0
        for a in list(data.get("bank_accounts", {}).values()):
            opening += float(a.get("current_balance", 0.0))
        import datetime as _dt
        today = _dt.datetime.fromisoformat("2024-11-30")
        inv_ids = [i.get("invoice_id") for i in list(data.get("invoices", {}).values()) if i.get("invoice_id") in ("INV008","INV009","INV010")]
        inflows_tool = ForecastInflows()
        infl = json.loads(inflows_tool.invoke(data,invoices=inv_ids,probability_rule="overdue_60=0.3"))
        outflows_tool = ForecastOutflows()
        out = json.loads(outflows_tool.invoke(data,recurring_schedules=True,taxes=True,horizon_months=horizon))
        closing = round(opening + float(infl.get("total_expected_inflows", 0.0)) - float(out.get("total_expected_outflows", 0.0)), 2)
        return json.dumps({"as_of": today.date().isoformat(),"granularity": gran,"horizon_months": horizon,"opening_balance": round(opening, 2),"expected_inflows": infl,"expected_outflows": out,"projected_closing_balance": closing}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function","function": {"name": "build_cashflow_view","description": "Build a simple monthly cashflow projection combining opening balance, inflows and outflows.","parameters": {"type": "object","properties": {"horizon_months": {"type": "integer"},"granularity": {"type": "string"}}}}}