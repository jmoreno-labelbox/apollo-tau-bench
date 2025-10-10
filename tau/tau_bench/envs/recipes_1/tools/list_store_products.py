# Sierra copyright

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _json_dump


class ListStoreProducts(Tool):
    """List store_products for a store (optionally filtered by ingredient_id)."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        store_id = kwargs.get("store_id")
        ingredient_id = kwargs.get("ingredient_id")
        if store_id is None:
            return _json_dump({"error": "store_id is required"})
        rows = [p for p in list(data.get("store_products", {}).values()) if int(p.get("store_id")) == int(store_id)]
        if ingredient_id is not None:
            rows = [p for p in rows if int(p.get("ingredient_id")) == int(ingredient_id)]
        return _json_dump(rows)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"list_store_products",
            "description":"List products for a store, optionally for an ingredient.",
            "parameters":{"type":"object","properties":{
                "store_id":{"type":"integer"},
                "ingredient_id":{"type":"integer"}
            },"required":["store_id"]}
        }}
