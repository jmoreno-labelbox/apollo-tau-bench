# Copyright © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetProductById(Tool):
    """Return a product by product_id."""
    @staticmethod
    def invoke(data, product_id) -> str:
        if not product_id:
            return json.dumps({"error":"product_id is required"}, indent=2)
        prod = next((p for p in list(data.get('products', {}).values()) if p.get('product_id') == product_id), None)
        return json.dumps(prod or {"error": f"product_id {product_id} not found"}, indent=2)

    @staticmethod
    def get_info():
        return {"type":"function","function":{"name":"get_product_by_id","description":"Get a product by product_id.","parameters":{"type":"object","properties":{"product_id":{"type":"string"}},"required":["product_id"]}}}
