# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetVenueByName(Tool):
    """Fetch a venue record by its venue_name (exact, case-sensitive)."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        name = kwargs.get("name")

        # 1) Validate
        if not isinstance(name, str) or name == "":
            return json.dumps({"error": "Missing required field: name"}, indent=2)

        # 2) Get DB
        venues: List[Dict[str, Any]] = list(data.get("venues", {}).values())

        # 3) Exact match (no normalization)
        for venue in venues:
            if venue.get("venue_name") == name:
                return json.dumps(venue, indent=2)

        return json.dumps({"error": f"No venue found with name {name}"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_venue_by_name",
                "description": "Fetch a single venue's full details by exact venue_name (case-sensitive).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "name": {
                            "type": "string",
                            "description": "Exact venue name to retrieve (e.g., 'New York Stadium')."
                        }
                    },
                    "required": ["name"]
                }
            }
        }
