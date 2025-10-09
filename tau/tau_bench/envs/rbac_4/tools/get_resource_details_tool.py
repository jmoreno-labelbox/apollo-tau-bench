from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetResourceDetailsTool(Tool):
    """Get information regarding a specified resource."""

    @staticmethod
    def invoke(data: dict[str, Any], resource_id: str = None) -> str:
        rid = resource_id
        for res in data.get("resources", []):
            if res["resource_id"] == rid:
                payload = res
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"Resource {rid} not found"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetResourceDetails",
                "description": "Get full details of a resource from resource_id",
                "parameters": {
                    "type": "object",
                    "properties": {"resource_id": {"type": "string"}},
                    "required": ["resource_id"],
                },
            },
        }
