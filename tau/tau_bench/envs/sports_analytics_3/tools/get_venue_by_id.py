# Sierra Copyright

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetVenueById(Tool):
    """Fetch a venue record by its venue_id."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        venue_id = kwargs.get("venue_id")

        # 1) Verify
        if venue_id is None:
            return json.dumps({"error": "Missing required field: venue_id"}, indent=2)

        # Retrieve the database from the provided data.
        venues: List[Dict[str, Any]] = list(data.get("venues", {}).values())

        # 3) Precise match retrieval
        for venue in venues:
            if venue.get("venue_id") == venue_id:
                return json.dumps(venue, indent=2)

        return json.dumps({"error": f"No venue found with ID {venue_id}"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_venue_by_id",
                "description": "Fetch a single venue's full details by venue_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "venue_id": {
                            "type": "integer",
                            "description": "Exact venue ID to retrieve."
                        }
                    },
                    "required": ["venue_id"]
                }
            }
        }
