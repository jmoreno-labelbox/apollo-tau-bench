# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class SetVariantAvailability(Tool):
    """Set a variant's 'available' flag."""
    @staticmethod
    def invoke(data, available, item_id) -> str:
        if item_id is None or available is None:
            return json.dumps({"error":"item_id and available are required"}, indent=2)
        prod, variant = _find_product_by_item(data, item_id)
        if not prod:
            return json.dumps({"error":f"item_id {item_id} not found"}, indent=2)
        prod['variants'][item_id]['available'] = bool(available)
        return json.dumps({"success": True, "item_id": item_id, "available": bool(available)}, indent=2)

    @staticmethod
    def get_info():
        return {"type":"function","function":{"name":"set_variant_availability","description":"Set the boolean 'available' flag for a variant.","parameters":{"type":"object","properties":{"item_id":{"type":"string"},"available":{"type":"boolean"}},"required":["item_id","available"]}}}
