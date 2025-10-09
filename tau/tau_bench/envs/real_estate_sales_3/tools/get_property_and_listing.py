from tau_bench.envs.tool import Tool
import json
from typing import Any

class GetPropertyAndListing(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], property_id: str = None) -> str:
        if not property_id:
            payload = {"error": "property_id is required"}
            out = json.dumps(payload, indent=2)
            return out
        prop = next(
            (
                p
                for p in data.get("properties", [])
                if p.get("property_id") == property_id
            ),
            None,
        )
        if not prop:
            payload = {"error": f"Property '{property_id}' not found"}
            out = json.dumps(
                payload, indent=2
            )
            return out
        listings = [
            l for l in data.get("listings", []) if l.get("property_id") == property_id
        ]
        listing = None
        if listings:
            listing = max(
                listings,
                key=lambda x: (x.get("updated_at") or "", x.get("listing_id", 0)),
            )
        payload = {"property": prop, "listing": listing}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getPropertyAndListing",
                "description": "Get a property's details and its most recent listing (if available).",
                "parameters": {
                    "type": "object",
                    "properties": {"property_id": {"type": "string"}},
                    "required": ["property_id"],
                },
            },
        }
