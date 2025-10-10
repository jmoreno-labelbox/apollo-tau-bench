# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ComputeTaxReserve(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        year = kwargs.get("tax_year")
        revenue = kwargs.get("ytd_revenue")
        if year is None or revenue is None:
            return json.dumps({"error": "tax_year and ytd_revenue are required"}, indent=2)
        rate = next((t["rate_percent"] for t in data.get("tax_rates", []) if t.get("tax_year") == year), None)
        if rate is None:
            return json.dumps({"error": f"No tax rate for {year}"}, indent=2)
        reserve = round(float(revenue) * (float(rate) / 100.0), 2)
        return json.dumps({"ytd_revenue": revenue,"tax_year": year,"tax_rate": rate,"tax_reserve": reserve}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function","function": {"name": "compute_tax_reserve","description": "Compute tax reserve given YTD revenue and tax year.","parameters": {"type": "object","properties": {"ytd_revenue": {"type": "number"},"tax_year": {"type": "integer"}},"required": ["ytd_revenue","tax_year"]}}}
