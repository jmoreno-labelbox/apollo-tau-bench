# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetPropertyAndListing(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        property_id = kwargs.get("property_id")
        if not property_id:
            return json.dumps({"error": "property_id is required"}, indent=2)
        prop = next((p for p in list(data.get("properties", {}).values()) if p.get("property_id") == property_id), None)
        if not prop:
            return json.dumps({"error": f"Property '{property_id}' not found"}, indent=2)
        listings = [l for l in list(data.get("listings", {}).values()) if l.get("property_id") == property_id]
        listing = None
        if listings:
            listing = max(listings, key=lambda x: (x.get("updated_at") or "", x.get("listing_id", 0)))
        return json.dumps({"property": prop, "listing": listing}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"get_property_and_listing",
            "description":"Get a property's details and its most recent listing (if available).",
            "parameters":{"type":"object","properties":{"property_id":{"type":"string"}},"required":["property_id"]}
        }}
