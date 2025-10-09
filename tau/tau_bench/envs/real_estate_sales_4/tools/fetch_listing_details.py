from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class FetchListingDetails(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], listing_id: str = None) -> str:
        if not listing_id:
            payload = {"error": "listing_id is required"}
            out = json.dumps(payload, indent=2)
            return out

        listings = data.get("listings", [])
        listing = next((l for l in listings if l.get("listing_id") == listing_id), None)

        if not listing:
            payload = {"error": f"Listing {listing_id} not found"}
            out = json.dumps(payload, indent=2)
            return out
        payload = listing
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FetchListingDetails",
                "description": "Fetch detailed information about a specific property listing",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "listing_id": {
                            "type": "integer",
                            "description": "The unique identifier for the listing",
                        }
                    },
                    "required": ["listing_id"],
                },
            },
        }
