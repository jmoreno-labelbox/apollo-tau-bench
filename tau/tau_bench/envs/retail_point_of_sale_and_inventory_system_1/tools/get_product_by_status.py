# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetProductByStatus(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        status = kwargs.get('status')
        products = list(data.get("products", {}).values())  # Lista []
        results = [product for product in products if product.get("status") == status]
        return json.dumps(results)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_product_by_status",
                "description": "Retrieves products with a specific status (e.g., 'active', 'discontinued', 'clearance', 'limited_availability').",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "status": {
                            "type": "string",
                            "description": "The status of the products to retrieve.",
                        },
                    },
                    "required": ["status"],
                },
            },
        }
