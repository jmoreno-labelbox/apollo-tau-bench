# Copyright Sierra

import requests
import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateAccessRequest(Tool):
    """ Creates a new access request for a user to receive a specific role for a resource. """

    @staticmethod
    def invoke(data: Dict[str, Any], justification, resource_id, role_id, timestamp, user_id) -> str:
        try:
            requests = data.get('access_requests', [])
        except (KeyError, json.JSONDecodeError):
            requests = []

        existing_ids = [int(r["request_id"].replace("AR-", "")) for r in requests if r.get("request_id", "").startswith("AR-")]
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
            "decision_at": None
        }

        requests.append(new_request)
        data["access_requests.json"] = json.dumps(requests, indent=4)

        return json.dumps(new_request)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_access_request",
                "description": "Submits a request for a user to be granted a role. Requires subsequent approval.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "The ID of the user who will receive the role."
                        },
                        "resource_id": {
                            "type": "string",
                            "description": "The ID of the resource the role applies to."
                        },
                        "role_id": {
                            "type": "string",
                            "description": "The ID of the requested role."
                        },
                        "justification": {
                            "type": "string",
                            "description": "A brief reason for the request."
                        },
                        "timestamp": {
                            "type": "string",
                            "description": "The current timestamp for when the request is submitted."
                        }
                    },
                    "required": ["user_id", "resource_id", "role_id", "justification"]
                }
            }
        }
