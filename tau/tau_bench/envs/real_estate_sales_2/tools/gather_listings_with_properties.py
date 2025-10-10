# Copyright © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GatherListingsWithProperties(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        ids = set(kwargs.get("listing_ids") or [])
        props = _by_key(list(data.get("properties", {}).values()), "property_id")
        out: List[Dict[str, Any]] = []
        for lst in (list(data.get("listings", {}).values()) or []):
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
