from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any

class GetProducts(Tool):
    """Fetches all IDs of products."""

    @staticmethod
    def invoke(data: dict[str, Any]) -> str:
        products = data.get("dim_product", [])
        ids_ = []
        for i in products:
            ids_ += [i.get("product_id")]
        payload = {"product_ids": ids_}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getProducts",
                "description": "Retrieves all product IDs.",
                "parameters": {},
            },
        }
