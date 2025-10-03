from tau_bench.envs.tool import Tool
import json
from typing import Any

class ForecastOutflows(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], recurring_schedules: bool = True, taxes: bool = True, horizon_months: int = 3) -> str:
        include_sched = bool(recurring_schedules)
        include_taxes = bool(taxes)
        horizon_months = int(horizon_months)
        total = 0.0
        lines: list[dict[str, Any]] = []
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
                lines.append(
                    {
                        "schedule_id": s.get("schedule_id"),
                        "frequency": freq,
                        "instances": count,
                        "amount_per_instance": amt,
                        "total": round(amt * count, 2),
                    }
                )
        if include_taxes:
            taxes = [
                s
                for s in data.get("recurring_schedules", [])
                if s.get("schedule_type") in ("tax_payment",)
            ]
            for t in taxes:
                amt = float(t.get("amount", 0.0))
                total += amt
                lines.append(
                    {
                        "schedule_id": t.get("schedule_id"),
                        "frequency": t.get("frequency"),
                        "instances": 1,
                        "amount_per_instance": amt,
                        "total": amt,
                        "type": "tax",
                    }
                )
        payload = {"total_expected_outflows": round(total, 2), "lines": lines}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ForecastOutflows",
                "description": "Forecast expected outflows from recurring schedules and taxes.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "recurring_schedules": {"type": "boolean"},
                        "taxes": {"type": "boolean"},
                        "horizon_months": {"type": "integer"},
                    },
                },
            },
        }
