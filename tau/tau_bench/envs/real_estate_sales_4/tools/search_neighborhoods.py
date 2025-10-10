# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class SearchNeighborhoods(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        city = kwargs.get('city')
        min_avg_price = kwargs.get('min_avg_price', 0)
        max_avg_price = kwargs.get('max_avg_price', float('inf'))
        
        neighborhoods = data.get('neighborhoods', [])
        results = []
        
        for neighborhood in neighborhoods:
            avg_price = neighborhood.get('avg_home_price', 0)
            if city and city.lower() not in neighborhood.get('city', '').lower():
                continue
            if not (min_avg_price <= avg_price <= max_avg_price):
                continue
            results.append(neighborhood)
        
        return json.dumps({
            "search_criteria": {
                "city": city,
                "min_avg_price": min_avg_price,
                "max_avg_price": max_avg_price
            },
            "neighborhood_count": len(results),
            "neighborhoods": results
        }, indent=2)
    
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "search_neighborhoods",
                "description": "Search for neighborhoods based on criteria",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "city": {
                            "type": "string",
                            "description": "City to search in"
                        },
                        "min_avg_price": {
                            "type": "number",
                            "description": "Minimum average home price"
                        },
                        "max_avg_price": {
                            "type": "number",
                            "description": "Maximum average home price"
                        }
                    },
                    "required": []
                }
            }
        }
