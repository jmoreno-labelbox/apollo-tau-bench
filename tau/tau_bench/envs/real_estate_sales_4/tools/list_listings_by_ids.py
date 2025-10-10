# Copyright Sierra Technologies

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ListListingsByIds(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        listing_ids = kwargs.get('listing_ids')
        if not listing_ids:
            return json.dumps({"error": "listing_ids is required"}, indent=2)
        
        listings = list(data.get('listings', {}).values())
        found_listings = []
        
        for listing_id in listing_ids:
            listing = next((l for l in listings if l.get('listing_id') == listing_id), None)
            if listing:
                found_listings.append(listing)
        
        return json.dumps({
            "requested_ids": listing_ids,
            "found_count": len(found_listings),
            "listings": found_listings
        }, indent=2)
    
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_listings_by_ids",
                "description": "Get multiple listings by their IDs",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "listing_ids": {
                            "type": "array",
                            "items": {"type": "integer"},
                            "description": "List of listing IDs to retrieve"
                        }
                    },
                    "required": ["listing_ids"]
                }
            }
        }
