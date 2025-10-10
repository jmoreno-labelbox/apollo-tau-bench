# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetProductPriceOnDate(Tool):
    """Looks up the price of a product on a specific date."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        product_id, query_date = kwargs.get("product_id"), kwargs.get("date")
        for entry in data.get('f_price', []):
            if entry.get('product_id') == product_id and entry.get('date') == query_date:
                return json.dumps(entry)
        return json.dumps({"error": "Price not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "get_product_price_on_date", "description": "Retrieves the price of a specific product on a given date.", "parameters": {"type": "object", "properties": {"product_id": {"type": "string"}, "date": {"type": "string"}}, "required": ["product_id", "date"]}}}
