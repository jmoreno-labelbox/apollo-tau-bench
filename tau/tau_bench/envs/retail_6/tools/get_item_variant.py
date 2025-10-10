# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetItemVariant(Tool):
    """Return product and variant by item_id."""
    @staticmethod
    def invoke(data, **kwargs) -> str:
        item_id = kwargs.get('item_id')
        if not item_id:
            return json.dumps({"error":"item_id is required"}, indent=2)
        prod, variant = _find_product_by_item(data, item_id)
        if not prod:
            return json.dumps({"error":f"item_id {item_id} not found"}, indent=2)
        return json.dumps({"product_id": prod['product_id'], "variant": variant}, indent=2)

    @staticmethod
    def get_info():
        return {"type":"function","function":{"name":"get_item_variant","description":"Return the variant record and product_id for a given item_id.","parameters":{"type":"object","properties":{"item_id":{"type":"string"}},"required":["item_id"]}}}
