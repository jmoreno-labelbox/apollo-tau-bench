from tau_bench.envs.tool import Tool
import json
from typing import Any

class ComputeYtdFromMonthlyRevenue(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], year: int = None, through_month: int = None) -> str:
        if not year or not through_month:
            payload = {"error": "year and through_month are required"}
            out = json.dumps(
                payload, indent=2
            )
            return out
        rows = [
            r
            for r in data.get("monthly_revenue", [])
            if str(r.get("month_year", "")).startswith(f"{year}-")
        ]
        total = 0.0
        for r in rows:
            try:
                m = int(r["month_year"].split("-")[1])
                if m <= through_month:
                    total += float(r.get("revenue", 0.0))
            except Exception:
                continue
        payload = {"year": year, "through_month": through_month, "ytd_revenue": round(total, 2)}
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info(self=None) -> dict[str, Any]:
        pass
        return {
            "type": "function",
            "function": {
                "name": "ComputeYtdFromMonthlyRevenue",
                "description": "Compute YTD revenue summing monthly_revenue rows up to a month.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "year": {"type": "integer"},
                        "through_month": {"type": "integer"},
                    },
                    "required": ["year", "through_month"],
                },
            },
        }
