from tau_bench.envs.tool import Tool
import json
import re
from datetime import datetime
from typing import Any

class GetProductByStatus(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], status: str = None) -> str:
        products = data.get("products", [])
        results = [product for product in products if product.get("status") == status]
        payload = results
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getProductByStatus",
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
