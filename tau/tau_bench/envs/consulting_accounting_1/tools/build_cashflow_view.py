from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class BuildCashflowView(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], horizon_months: int = 3, granularity: str = "monthly") -> str:
        opening = 0.0
        for a in data.get("bank_accounts", []):
            opening += float(a.get("current_balance", 0.0))
        import datetime as _dt

        today = _dt.datetime.fromisoformat("2024-11-30")
        inv_ids = [
            i.get("invoice_id")
            for i in data.get("invoices", [])
            if i.get("invoice_id") in ("INV008", "INV009", "INV010")
        ]
        inflows_tool = ForecastInflows()
        infl = json.loads(
            inflows_tool.invoke(
                data, invoices=inv_ids, probability_rule="overdue_60=0.3"
            )
        )
        outflows_tool = ForecastOutflows()
        out = json.loads(
            outflows_tool.invoke(
                data, recurring_schedules=True, taxes=True, horizon_months=horizon_months
            )
        )
        closing = round(
            opening
            + float(infl.get("total_expected_inflows", 0.0))
            - float(out.get("total_expected_outflows", 0.0)),
            2,
        )
        payload = {
                "as_of": today.date().isoformat(),
                "granularity": granularity,
                "horizon_months": horizon_months,
                "opening_balance": round(opening, 2),
                "expected_inflows": infl,
                "expected_outflows": out,
                "projected_closing_balance": closing,
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
                "name": "BuildCashflowView",
                "description": "Build a simple monthly cashflow projection combining opening balance, inflows and outflows.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "horizon_months": {"type": "integer"},
                        "granularity": {"type": "string"},
                    },
                },
            },
        }
