# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetProductDetails(Tool):
    """A tool to retrieve all master data for a specific product by its name."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        product_name = kwargs.get('product_name')
        if not product_name:
            return json.dumps({"error": "product_name is a required argument."}, indent=2)
        product_master = list(data.get('product_master', {}).values())
        product = next((p for p in product_master if p.get('product_name') == product_name), None)
        if product:
            return json.dumps(product, indent=2)
        return json.dumps({"error": f"Product '{product_name}' not found."}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "get_product_details", "description": "Retrieves all master data for a specific product by its exact name.", "parameters": {"type": "object", "properties": {"product_name": {"type": "string", "description": "The full, exact name of the product to search for."}}, "required": ["product_name"]}}}
