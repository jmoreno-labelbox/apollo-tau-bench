# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetComparableProperties(Tool):
    """Get comparable properties for a specific property."""
    
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        property_id = kwargs.get('property_id')
        if not property_id:
            return json.dumps({"error": "property_id is required"}, indent=2)
        
        # Get comparables for property
        comparables = data.get('comparables', [])
        property_comps = [c for c in comparables if c.get('property_id') == property_id]
        
        return json.dumps({
            "property_id": property_id,
            "comparable_count": len(property_comps),
            "comparables": property_comps
        }, indent=2)
    
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_comparable_properties",
                "description": "Get comparable properties for a specific property",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "property_id": {
                            "type": "string",
                            "description": "Property ID to get comparables for"
                        }
                    },
                    "required": ["property_id"]
                }
            }
        }
