# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool




def _by_key(items: List[Dict[str, Any]], key: str) -> Dict[Any, Dict[str, Any]]:
    return {i.get(key): i for i in (items or [])}

class GatherListingsWithProperties(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], listing_ids) -> str:
        ids = set(listing_ids or [])
        props = _by_key(list(list(list(data.get("properties", {}).values())) if isinstance(data.get("properties"), dict) else data.get("properties", [])), "property_id")
        out: List[Dict[str, Any]] = []
        for lst in (list(list(list(data.get("listings", {}).values())) if isinstance(data.get("listings"), dict) else data.get("listings", [])) or []):
            if ids and lst.get("listing_id") not in ids:
                continue
            pr = props.get(lst.get("property_id")) or {}
            out.append({"listing": lst, "property": pr})
        return json.dumps({"items": out}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "gather_listings_with_properties",
                "description": "Return listing + property for listing_ids.",
                "parameters": {
                    "type": "object",
                    "properties": {"listing_ids": {"type": "array", "items": {"type": "integer"}}},
                    "required": ["listing_ids"],
                },
            },
        }