from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetAccessRequestTool(Tool):
    """Get a single access request using its ID (read-only, predictable)."""

    @staticmethod
    def invoke(data: dict[str, Any], request_id: str = None) -> str:
        pass
        # Anticipate: data["access_requests"] is a collection of dicts sourced from /mnt/data/access_requests.json
        access_requests = data.get("access_requests", [])
        if not isinstance(access_requests, list):
            payload = {"error": "access_requests must be a list"}
            out = json.dumps(payload, indent=2)
            return out

        if not isinstance(request_id, str) or not request_id.strip():
            payload = {"error": "request_id must be a non-empty string"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        # Lookup in read-only mode
        for row in access_requests:
            if isinstance(row, dict) and row.get("request_id") == request_id:
                payload = {"access_request": row}
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"Access request {request_id} not found"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetAccessRequest",
                "description": "Retrieve a single access request by ID (read-only).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "request_id": {
                            "type": "string",
                            "description": "Access request ID, e.g. AR-004",
                        }
                    },
                    "required": ["request_id"],
                },
            },
        }
