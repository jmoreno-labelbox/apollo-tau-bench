from tau_bench.envs.tool import Tool
import json
from typing import Any

class ComputeTaxReserve(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], tax_year: int = None, ytd_revenue: float = None) -> str:
        year = tax_year
        revenue = ytd_revenue
        if year is None or revenue is None:
            payload = {"error": "tax_year and ytd_revenue are required"}
            out = json.dumps(
                payload, indent=2
            )
            return out
        rate = next(
            (
                t["rate_percent"]
                for t in data.get("tax_rates", [])
                if t.get("tax_year") == year
            ),
            None,
        )
        if rate is None:
            payload = {"error": f"No tax rate for {year}"}
            out = json.dumps(payload, indent=2)
            return out
        reserve = round(float(revenue) * (float(rate) / 100.0), 2)
        payload = {
                "ytd_revenue": revenue,
                "tax_year": year,
                "tax_rate": rate,
                "tax_reserve": reserve,
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
                "name": "ComputeTaxReserve",
                "description": "Compute tax reserve given YTD revenue and tax year.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "ytd_revenue": {"type": "number"},
                        "tax_year": {"type": "integer"},
                    },
                    "required": ["ytd_revenue", "tax_year"],
                },
            },
        }
