from tau_bench.envs.tool import Tool
import json
from typing import Any

class GetVenueById(Tool):
    """Retrieve a venue record using its venue_id."""

    @staticmethod
    def invoke(data: dict[str, Any], venue_id: str = None) -> str:
        #1) Confirm validity
        if venue_id is None:
            payload = {"error": "Missing required field: venue_id"}
            out = json.dumps(payload, indent=2)
            return out

        #2) Retrieve DB using provided data
        venues: list[dict[str, Any]] = data.get("venues", [])

        #3) Lookup for exact matches
        for venue in venues:
            if venue.get("venue_id") == venue_id:
                payload = venue
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"No venue found with ID {venue_id}"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetVenueById",
                "description": "Fetch a single venue's full details by venue_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "venue_id": {
                            "type": "integer",
                            "description": "Exact venue ID to retrieve.",
                        }
                    },
                    "required": ["venue_id"],
                },
            },
        }
