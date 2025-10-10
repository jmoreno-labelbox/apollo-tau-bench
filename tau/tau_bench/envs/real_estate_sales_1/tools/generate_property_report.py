# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GeneratePropertyReport(Tool):
    """Generate a comprehensive report for a property including comparables."""
    
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        property_id = kwargs.get('property_id')
        if not property_id:
            return json.dumps({"error": "property_id is required"}, indent=2)
        
        # Get property listing
        listings = list(data.get('listings', {}).values())
        listing = next((l for l in listings if l.get('property_id') == property_id), None)
        
        if not listing:
            return json.dumps({
                "error": f"Property {property_id} not found"
            }, indent=2)
        
        # Get comparables
        comparables = list(data.get('comparables', {}).values())
        property_comparables = [c for c in comparables if c.get('property_id') == property_id]
        
        # Calculate market analysis
        all_prices = [c.get('comparable_price', 0) for c in property_comparables]
        if all_prices:
            avg_comparable_price = sum(all_prices) / len(all_prices)
            price_variance = listing.get('list_price', 0) - avg_comparable_price
        else:
            avg_comparable_price = 0
            price_variance = 0
        
        report = {
            "property_id": property_id,
            "listing_details": listing,
            "market_analysis": {
                "comparable_count": len(property_comparables),
                "average_comparable_price": round(avg_comparable_price, 2),
                "price_variance": round(price_variance, 2),
                "price_competitive": abs(price_variance) < 50000
            },
            "comparables": property_comparables,
            "report_generated_at": "2024-08-21T00:00:00Z"
        }
        
        return json.dumps(report, indent=2)
    
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "generate_property_report",
                "description": "Generate a comprehensive property report with market analysis",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "property_id": {
                            "type": "string",
                            "description": "Property ID to generate report for"
                        }
                    },
                    "required": ["property_id"]
                }
            }
        }
