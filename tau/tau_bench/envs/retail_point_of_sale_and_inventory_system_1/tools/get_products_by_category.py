# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetProductsByCategory(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        category = kwargs.get('category')
        products = list(data.get("products", {}).values())  # Lista []
        results = [product for product in products if product.get("category") == category]
        return json.dumps(results)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_products_by_category",
                "description": "Retrieves all products that belong to a specific category.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "status": {
                            "type": "string",
                            "description": "The category of the products to retrieve.",
                        },
                    },
                    "required": ["category"],
                },
            },
        }
