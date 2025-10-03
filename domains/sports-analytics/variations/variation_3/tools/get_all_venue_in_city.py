from tau_bench.envs.tool import Tool
import json
from typing import Any

class GetAllVenueInCity(Tool):
    """Retrieve all venues situated in a specific city (exact, case-sensitive)."""

    @staticmethod
    def invoke(data: dict[str, Any], city: str = None) -> str:
        #1) Confirm validity
        if not isinstance(city, str) or city == "":
            payload = {"error": "Missing required field: city"}
            out = json.dumps(payload, indent=2)
            return out

        #2) Retrieve DB
        venues: list[dict[str, Any]] = data.get("venues", [])

        #3) Filter for exact city
        matching = [v for v in venues if v.get("city") == city]

        if not matching:
            payload = {"error": f"No venues found in city {city}"}
            out = json.dumps(payload, indent=2)
            return out
        payload = matching
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetAllVenueInCity",
                "description": "Fetch all venue records whose city exactly matches the provided value (case-sensitive).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "city": {
                            "type": "string",
                            "description": "Exact city name (e.g., 'Kansas City').",
                        }
                    },
                    "required": ["city"],
                },
            },
        }
