# Copyright Sierra Technologies

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetTaxRate(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        """
        Returns tax_rate_id(s). Optionally filter by year.
        """
        year = kwargs.get("year")
        if year:
            ids = [t["tax_rate_id"] for t in data["tax_rates"] if t.get("year") == year]
        else:
            ids = [t["tax_rate_id"] for t in data["tax_rates"]]
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
