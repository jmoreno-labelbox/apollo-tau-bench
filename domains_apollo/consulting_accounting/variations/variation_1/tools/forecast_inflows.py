from tau_bench.envs.tool import Tool
import json
from typing import Any

class ForecastInflows(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], invoices: list = None, probability_rule: str = "overdue_60=0.3") -> str:
        invoices_ids = invoices if invoices is not None else []
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
            breakdown.append(
                {
                    "invoice_id": inv_id,
                    "days_overdue": days,
                    "amount": amt,
                    "probability": prob,
                    "expected": expected,
                }
            )
        payload = {
                "total_expected_inflows": round(total_expected, 2),
                "breakdown": breakdown,
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
                "name": "ForecastInflows",
                "description": "Forecast expected inflows from invoices (discount >60d overdue).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "invoices": {"type": "array", "items": {"type": "string"}},
                        "probability_rule": {"type": "string"},
                    },
                    "required": ["invoices"],
                },
            },
        }
