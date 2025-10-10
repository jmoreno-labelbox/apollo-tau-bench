# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ForecastOutflows(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        include_sched = bool(kwargs.get("recurring_schedules", True))
        include_taxes = bool(kwargs.get("taxes", True))
        horizon_months = int(kwargs.get("horizon_months", 3))
        total = 0.0
        lines: List[Dict[str, Any]] = []
        if include_sched:
            for s in list(data.get("recurring_schedules", {}).values()):
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
            taxes = [s for s in list(data.get("recurring_schedules", {}).values()) if s.get("schedule_type") in ("tax_payment",)]
            for t in taxes:
                amt = float(t.get("amount", 0.0))
                total += amt
                lines.append({"schedule_id": t.get("schedule_id"),"frequency": t.get("frequency"),"instances": 1,"amount_per_instance": amt,"total": amt,"type": "tax"})
        return json.dumps({"total_expected_outflows": round(total, 2),"lines": lines}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function","function": {"name": "forecast_outflows","description": "Forecast expected outflows from recurring schedules and taxes.","parameters": {"type": "object","properties": {"recurring_schedules": {"type": "boolean"},"taxes": {"type": "boolean"},"horizon_months": {"type": "integer"}}}}}
