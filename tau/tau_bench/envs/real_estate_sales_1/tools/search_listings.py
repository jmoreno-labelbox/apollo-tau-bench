# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class SearchListings(Tool):
    """Search for property listings by various criteria."""
    
    @staticmethod
    def invoke(data: Dict[str, Any], property_id, status, max_price = float('inf'), min_price = 0) -> str:
        listings = list(data.get('listings', {}).values())
        results = []
        
        for listing in listings:
            # Apply criteria-based filtering.
            if property_id and listing.get('property_id') != property_id:
                continue
            if status and listing.get('status') != status:
                continue
            
            price = listing.get('list_price', 0)
            if not (min_price <= price <= max_price):
                continue
                
            results.append(listing)
        
        return json.dumps(results, indent=2)
    
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "search_listings",
                "description": "Search for property listings matching specific criteria",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "status": {
                            "type": "string",
                            "description": "Listing status (for_sale, sold, pending, etc.)"
                        },
                        "min_price": {
                            "type": "number",
                            "description": "Minimum price range"
                        },
                        "max_price": {
                            "type": "number",
                            "description": "Maximum price range"
                        },
                        "property_id": {
                            "type": "string",
                            "description": "Specific property ID to search for"
                        }
                    },
                    "required": []
                }
            }
        }
