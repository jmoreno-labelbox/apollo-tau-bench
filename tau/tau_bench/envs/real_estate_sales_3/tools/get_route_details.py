from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetRouteDetails(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], route_id: str = None) -> str:
        rid = route_id
        r = next((x for x in data.get("routes", []) if x.get("route_id") == rid), None)
        if not r:
            payload = {"error": f"route_id {rid} not found"}
            out = json.dumps(payload, indent=2)
            return out
        payload = r
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetRouteDetails",
                "description": "Fetch a route by ID.",
                "parameters": {
                    "type": "object",
                    "properties": {"route_id": {"type": "integer"}},
                    "required": ["route_id"],
                },
            },
        }
