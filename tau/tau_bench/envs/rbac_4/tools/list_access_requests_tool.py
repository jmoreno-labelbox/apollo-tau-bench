from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class ListAccessRequestsTool(Tool):
    """Display access requests categorized by status or resource."""

    @staticmethod
    def invoke(data: dict[str, Any], status: str = None, resource_id: str = None) -> str:
        reqs = data.get("access_requests", {}).values()
        results = []
        for r in reqs:
            if status and r["status"] != status:
                continue
            if resource_id and r["resource_id"] != resource_id:
                continue
            results.append(r)
        payload = results
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ListAccessRequests",
                "description": "List access requests filtered by status or resource",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "status": {"type": "string"},
                        "resource_id": {"type": "string"},
                    },
                },
            },
        }
