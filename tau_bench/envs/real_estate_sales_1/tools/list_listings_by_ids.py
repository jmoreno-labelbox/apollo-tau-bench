from tau_bench.envs.tool import Tool
import json
from typing import Any

class ListListingsByIds(Tool):
    """Retrieve several listings using their identifiers."""

    @staticmethod
    def invoke(data: dict[str, Any], listing_ids: list[str] = None) -> str:
        if not listing_ids:
            payload = {"error": "listing_ids is required"}
            out = json.dumps(payload, indent=2)
            return out

        listings = data.get("listings", [])
        found_listings = []

        for listing_id in listing_ids:
            listing = next(
                (l for l in listings if l.get("listing_id") == listing_id), None
            )
            if listing:
                found_listings.append(listing)
        payload = {
                "requested_ids": listing_ids,
                "found_count": len(found_listings),
                "listings": found_listings,
            }
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "listListingsByIds",
                "description": "Get multiple listings by their IDs",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "listing_ids": {
                            "type": "array",
                            "items": {"type": "integer"},
                            "description": "List of listing IDs to retrieve",
                        }
                    },
                    "required": ["listing_ids"],
                },
            },
        }
