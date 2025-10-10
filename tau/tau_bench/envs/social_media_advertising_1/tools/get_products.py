# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetProducts(Tool):
    """Retrieves all product IDs."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        products = list(data.get("dim_product", {}).values())
        ids_ = []
        for i in products:
            ids_ += [i.get("product_id")]
        return json.dumps({"product_ids": ids_})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_products",
                "description": "Retrieves all product IDs.",
                "parameters": {},
            },
        }
