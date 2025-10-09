from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class FindListings(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], status: str = None, min_price: float = 0, max_price: float = float("inf"), property_id: str = None) -> str:
        listings = data.get("listings", [])
        results = []

        for listing in listings:
            if property_id and listing.get("property_id") != property_id:
                continue
            if status and listing.get("status") != status:
                continue

            price = listing.get("list_price", 0)
            if not (min_price <= price <= max_price):
                continue

            results.append(listing)
        payload = results
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "findListings",
                "description": "find property listings matching specific criteria",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "status": {
                            "type": "string",
                            "description": "Listing status (for_sale, sold, pending, etc.)",
                        },
                        "min_price": {
                            "type": "number",
                            "description": "Minimum price range",
                        },
                        "max_price": {
                            "type": "number",
                            "description": "Maximum price range",
                        },
                        "property_id": {
                            "type": "string",
                            "description": "Specific property ID to search for",
                        },
                    },
                    "required": [],
                },
            },
        }
