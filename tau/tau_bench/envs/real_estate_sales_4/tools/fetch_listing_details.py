# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class FetchListingDetails(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], listing_id) -> str:
        if not listing_id:
            return json.dumps({"error": "listing_id is required"}, indent=2)
        
        listings = list(data.get('listings', {}).values())
        listing = next((l for l in listings if l.get('listing_id') == listing_id), None)
        
        if not listing:
            return json.dumps({"error": f"Listing {listing_id} not found"}, indent=2)
        
        return json.dumps(listing, indent=2)
    
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "fetch_listing_details",
                "description": "Fetch detailed information about a specific property listing",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "listing_id": {
                            "type": "integer",
                            "description": "The unique identifier for the listing"
                        }
                    },
                    "required": ["listing_id"]
                }
            }
        }
