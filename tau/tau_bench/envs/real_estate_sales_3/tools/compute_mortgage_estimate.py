from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class ComputeMortgageEstimate(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], client_id: str = None, list_price: float = None, term_years: int = 30, region_override: str = None,
    region: Any = None,
    ) -> str:
        profiles = data.get("mortgage_profiles") or data.get("mortage_profiles") or []
        profile = next((m for m in profiles if m.get("client_id") == client_id), {})
        credit_score = profile.get("credit_score", 720)
        down_payment = profile.get("down_payment", int(0.2 * (list_price or 0)))
        loan_amount = profile.get(
            "desired_loan_amount", (list_price or 0) - down_payment
        )
        region = region_override or profile.get("region")

        best = None
        for r in data.get("mortgage_rates", []) or []:
            if region and r.get("region") != region:
                continue
            if r.get("term_years") != term_years:
                continue
            if r.get("min_credit_score", 0) > credit_score:
                continue
            if not best or r.get("apr_percent", 99) < best.get("apr_percent", 99):
                best = r
        apr = (best or {}).get("apr_percent", 6.0) / 100.0
        monthly_rate = apr / 12.0
        n = term_years * 12
        if monthly_rate == 0 or n == 0:
            monthly_payment = loan_amount / max(1, n)
        else:
            monthly_payment = (
                loan_amount
                * (monthly_rate * (1 + monthly_rate) ** n)
                / ((1 + monthly_rate) ** n - 1)
            )
        payload = {
                "client_id": client_id,
                "loan_amount": round(loan_amount, 2),
                "apr_percent": round(apr * 100, 3),
                "term_years": term_years,
                "estimated_monthly_payment": round(monthly_payment, 2),
                "lender_rate_used": best,
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
                "name": "ComputeMortgageEstimate",
                "description": "Estimate monthly payment for a client given list_price (prefers client profile + lender rates).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "client_id": {"type": "integer"},
                        "list_price": {"type": "number"},
                        "term_years": {"type": "integer"},
                        "region": {"type": "string"},
                    },
                    "required": ["client_id", "list_price"],
                },
            },
        }
