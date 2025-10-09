from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetProducts(Tool):
    """Fetches all IDs of products."""

    @staticmethod
    def invoke(data: dict[str, Any]) -> str:
        products = data.get("dim_product", {}).values()
        ids_ = []
        for i in products.values():
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
