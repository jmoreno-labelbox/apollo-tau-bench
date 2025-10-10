# Copyright © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetAllVenueInCity(Tool):
    """Fetch all venues located in a given city (exact, case-sensitive)."""

    @staticmethod
    def invoke(data: Dict[str, Any], city) -> str:

        # 1) Verify
        if not isinstance(city, str) or city == "":
            return json.dumps({"error": "Missing required field: city"}, indent=2)

        # Retrieve database.
        venues: List[Dict[str, Any]] = list(data.get("venues", {}).values())

        # 3) Filter by specific city
        matching = [v for v in venues if v.get("city") == city]

        if not matching:
            return json.dumps({"error": f"No venues found in city {city}"}, indent=2)

        return json.dumps(matching, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_all_venue_in_city",
                "description": "Fetch all venue records whose city exactly matches the provided value (case-sensitive).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "city": {
                            "type": "string",
                            "description": "Exact city name (e.g., 'Boston')."
                        }
                    },
                    "required": ["city"]
                }
            }
        }
