# Sierra Copyright

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool




class FindListings(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        listings = data.get('listings', [])
        results = []
        
        status = kwargs.get('status')
        min_price = kwargs.get('min_price', 0)
        max_price = kwargs.get('max_price', float('inf'))
        property_id = kwargs.get('property_id')
        
        for listing in listings:
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
                "name": "find_listings",
                "description": "find property listings matching specific criteria",
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

class FindListingsInNeighborhoods(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], neighborhood_ids) -> str:
        neighborhood_ids = neighborhood_ids or []
        return FindListings.invoke(data, **kwargs)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"find_listings_in_neighborhoods",
            "description":"Find listings within the provided neighborhoods.",
            "parameters":{
                "type":"object","properties":{
                    "neighborhood_ids":{"type":"array","items":{"type":"integer"}},
                    "price_min":{"type":"integer"},"price_max":{"type":"integer"},
                    "beds":{"type":"integer"},"baths":{"type":"integer"},"limit":{"type":"integer"}
                },"required":["neighborhood_ids"]
            }
        }}