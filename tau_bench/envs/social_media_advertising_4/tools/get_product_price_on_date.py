from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any

class GetProductPriceOnDate(Tool):
    """Finds the price of a product on a given date."""

    @staticmethod
    def invoke(data: dict[str, Any], product_id: str = None, query_date: str = None, date: Any = None) -> str:
        for entry in data.get("f_price", []):
            if (
                entry.get("product_id") == product_id
                and entry.get("date") == query_date
            ):
                payload = entry
                out = json.dumps(payload)
                return out
        payload = {"error": "Price not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetProductPriceOnDate",
                "description": "Retrieves the price of a specific product on a given date.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "product_id": {"type": "string"},
                        "date": {"type": "string"},
                    },
                    "required": ["product_id", "date"],
                },
            },
        }
