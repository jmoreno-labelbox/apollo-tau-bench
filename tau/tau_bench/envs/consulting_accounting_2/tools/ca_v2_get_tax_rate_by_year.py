# Copyright © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CaV2GetTaxRateByYear(Tool):
    """Get tax rate for a specific year."""

    @staticmethod
    def invoke(data: Dict[str, Any], year) -> str:
        if not year:
            return _error("year is required.")

        tax_rates = data.get("tax_rates", [])
        tax_rate = _find_one(tax_rates, "tax_year", int(year))
        return json.dumps(tax_rate) if tax_rate else _error(f"Tax rate for year {year} not found.")

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ca_v2_get_tax_rate_by_year",
                "description": "Get the tax rate for a specific year.",
                "parameters": {
                    "type": "object",
                    "properties": {"year": {"type": "string"}},
                    "required": ["year"],
                },
            },
        }
