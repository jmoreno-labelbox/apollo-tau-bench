from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timedelta
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class CaV2GetTaxRateByYear(Tool):
    """Retrieve the tax rate for a particular year."""

    @staticmethod
    def invoke(data: dict[str, Any], year: int = None) -> str:
        if not year:
            return _error("year is required.")

        tax_rates = data.get("tax_rates", [])
        tax_rate = _find_one(tax_rates, "tax_year", int(year))
        return (
            json.dumps(tax_rate)
            if tax_rate
            else _error(f"Tax rate for year {year} not found.")
        )

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CaV2GetTaxRateByYear",
                "description": "Get the tax rate for a specific year.",
                "parameters": {
                    "type": "object",
                    "properties": {"year": {"type": "string"}},
                    "required": ["year"],
                },
            },
        }
