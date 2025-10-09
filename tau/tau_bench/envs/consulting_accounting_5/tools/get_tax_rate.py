from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any, Dict
from datetime import timedelta

class GetTaxRate(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], year: int = None) -> str:
        """
        Returns tax_rate_id(s). Optionally filter by year.
        """
        if year:
            ids = [t["tax_rate_id"] for t in data["tax_rates"].values() if t.get("year") == year]
        else:
            ids = [t["tax_rate_id"] for t in data["tax_rates"].values()]
        return json.dumps(ids)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetTaxRate",
                "description": "Retrieve tax_rate_id(s), optionally filtered by year.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "year": {"type": "integer", "description": "Optional tax year filter"}
                    },
                    "required": [],
                },
            },
        }
