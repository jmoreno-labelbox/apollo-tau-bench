# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetProductBySKU(Tool):
    """Tool to retrieve a product by its SKU."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        sku = kwargs.get("sku")
        products = list(data.get("product_master", {}).values())
        for product in products:
            if product["sku"] == sku:
                return json.dumps(product, indent=2)
        return json.dumps({"error": f"SKU '{sku}' not found."}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_product_by_sku",
                "description": "Retrieve a product's full details using its SKU.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "sku": {
                            "type": "string",
                            "description": "Product SKU (e.g., 'PHRM-DRUG-S19')"
                        }
                    },
                    "required": ["sku"]
                }
            }
        }
