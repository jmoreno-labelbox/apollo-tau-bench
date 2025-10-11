# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class SetVariantPrice(Tool):
    """Set a variant's price to a specified numeric value."""
    @staticmethod
    def invoke(data, item_id, price) -> str:
        if item_id is None or price is None:
            return json.dumps({"error":"item_id and price are required"}, indent=2)
        prod, variant = _find_product_by_item(data, item_id)
        if not prod:
            return json.dumps({"error":f"item_id {item_id} not found"}, indent=2)
        prod['variants'][item_id]['price'] = float(price)
        return json.dumps({"success": True, "item_id": item_id, "price": float(price)}, indent=2)

    @staticmethod
    def get_info():
        return {"type":"function","function":{"name":"set_variant_price","description":"Set a specific variant price.","parameters":{"type":"object","properties":{"item_id":{"type":"string"},"price":{"type":"number"}},"required":["item_id","price"]}}}
