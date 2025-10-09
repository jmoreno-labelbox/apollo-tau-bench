from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timezone
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class FindAccessRequestByDetails(Tool):
    """Locate an access request by examining its content details."""

    @staticmethod
    def invoke(data: dict[str, Any], user_id: str = None, role_id: str = None, resource_id: str = None) -> str:
        try:
            access_requests = data.get("access_requests", [])
        except:
            access_requests = []

        for request in access_requests:
            if (
                request.get("user_id") == user_id
                and request.get("requested_role_id") == role_id
                and request.get("resource_id") == resource_id
            ):
                payload = request
                out = json.dumps(payload)
                return out
        payload = {"error": "No matching access request found for the provided details."}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FindAccessRequestByDetails",
                "description": "Finds a specific access request by searching for a combination of the user who requested it, the role they requested, and the resource they requested it for.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "The user ID of the requester.",
                        },
                        "role_id": {
                            "type": "string",
                            "description": "The role ID that was requested.",
                        },
                        "resource_id": {
                            "type": "string",
                            "description": "The resource ID that was requested.",
                        },
                    },
                    "required": ["user_id", "role_id", "resource_id"],
                },
            },
        }
