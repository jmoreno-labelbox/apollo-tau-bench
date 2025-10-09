from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetVenueByName(Tool):
    """Retrieve a venue record using its venue_name (exact, case-sensitive)."""

    @staticmethod
    def invoke(data: dict[str, Any], name: str = None) -> str:
        #1) Confirm validity
        if not isinstance(name, str) or name == "":
            payload = {"error": "Missing required field: name"}
            out = json.dumps(payload, indent=2)
            return out

        #2) Retrieve DB
        venues: list[dict[str, Any]] = data.get("venues", [])

        #3) Exact match (without normalization)
        for venue in venues:
            if venue.get("venue_name") == name:
                payload = venue
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"No venue found with name {name}"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getVenueByName",
                "description": "Fetch a single venue's full details by exact venue_name (case-sensitive).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "name": {
                            "type": "string",
                            "description": "Exact venue name to retrieve (e.g., 'Charlotte').",
                        }
                    },
                    "required": ["name"],
                },
            },
        }
