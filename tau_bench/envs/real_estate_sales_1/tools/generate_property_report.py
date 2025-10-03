from tau_bench.envs.tool import Tool
import json
from typing import Any

class GeneratePropertyReport(Tool):
    """Create a detailed report for a property that includes comparables."""

    @staticmethod
    def invoke(data: dict[str, Any], property_id: str = None) -> str:
        if not property_id:
            payload = {"error": "property_id is required"}
            out = json.dumps(payload, indent=2)
            return out

        # Fetch the property listing
        listings = data.get("listings", [])
        listing = next(
            (l for l in listings if l.get("property_id") == property_id), None
        )

        if not listing:
            payload = {"error": f"Property {property_id} not found"}
            out = json.dumps(payload, indent=2)
            return out

        # Retrieve comparable properties
        comparables = data.get("comparables", [])
        property_comparables = [
            c for c in comparables if c.get("property_id") == property_id
        ]

        # Perform market analysis
        all_prices = [c.get("comparable_price", 0) for c in property_comparables]
        if all_prices:
            avg_comparable_price = sum(all_prices) / len(all_prices)
            price_variance = listing.get("list_price", 0) - avg_comparable_price
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
                "price_competitive": abs(price_variance) < 50000,
            },
            "comparables": property_comparables,
            "report_generated_at": "2024-08-21T00:00:00Z",
        }
        payload = report
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "generatePropertyReport",
                "description": "Generate a comprehensive property report with market analysis",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "property_id": {
                            "type": "string",
                            "description": "Property ID to generate report for",
                        }
                    },
                    "required": ["property_id"],
                },
            },
        }
