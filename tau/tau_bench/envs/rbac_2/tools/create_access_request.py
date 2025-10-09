from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timezone
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class CreateAccessRequest(Tool):
    """Initiates a new access request for a user to obtain a particular role for a resource."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        user_id: str = None,
        resource_id: str = None,
        role_id: str = None,
        justification: str = None,
        timestamp: str = None
    ) -> str:
        try:
            requests = data.get("access_requests", {}).values()
        except (KeyError, json.JSONDecodeError):
            requests = []

        existing_ids = [
            int(r["request_id"].replace("AR-", ""))
            for r in requests.values() if r.get("request_id", "").startswith("AR-")
        ]
        next_id_num = max(existing_ids) + 1 if existing_ids else 1
        request_id = f"AR-{next_id_num:03d}"

        new_request = {
            "request_id": request_id,
            "user_id": user_id,
            "resource_id": resource_id,
            "requested_role_id": role_id,
            "justification": justification,
            "status": "PENDING",
            "submitted_at": timestamp,
            "reviewed_by": None,
            "decision_at": None,
        }

        data["access_requests"][new_request["access_request_id"]] = new_request
        data["access_requests.json"] = json.dumps(requests, indent=4)
        payload = new_request
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateAccessRequest",
                "description": "Submits a request for a user to be granted a role. Requires subsequent approval.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "The ID of the user who will receive the role.",
                        },
                        "resource_id": {
                            "type": "string",
                            "description": "The ID of the resource the role applies to.",
                        },
                        "role_id": {
                            "type": "string",
                            "description": "The ID of the requested role.",
                        },
                        "justification": {
                            "type": "string",
                            "description": "A brief reason for the request.",
                        },
                        "timestamp": {
                            "type": "string",
                            "description": "The current timestamp for when the request is submitted.",
                        },
                    },
                    "required": ["user_id", "resource_id", "role_id", "justification"],
                },
            },
        }
