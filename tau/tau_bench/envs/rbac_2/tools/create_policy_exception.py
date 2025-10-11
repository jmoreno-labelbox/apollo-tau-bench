# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreatePolicyException(Tool):
    """ Create a new policy exception for granting emergency access based on a specific permission. """

    @staticmethod
    def invoke(data: Dict[str, Any], approved_by, expires_on, justification, permission_id, timestamp, user_id) -> str:
        try:
            policy_exceptions = data.get('policy_exceptions', [])
        except:
            policy_exceptions = []

        existing_ids = [int(item["exception_id"].replace("PE-", "")) for item in policy_exceptions if
                        item.get("exception_id", "").startswith("PE-")]
        next_id_num = max(existing_ids) + 1 if existing_ids else 1
        exception_id = f"PE-{next_id_num:03d}"

        new_exception = {
            "exception_id": exception_id,
            "user_id": user_id,
            "permission_id": permission_id,
            "reviewed_by": approved_by,
            "requested_on": timestamp,
            "reviewed_on": timestamp,
            "expires_on": expires_on,
            "reason": justification,
            "status": "ACTIVE"
        }

        policy_exceptions.append(new_exception)
        data['policy_exceptions'] = policy_exceptions

        return json.dumps({
            "message": "Policy exception created successfully.",
            "exception_details": new_exception
        })

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_policy_exception",
                "description": "Creates a policy exception to grant temporary, emergency access for a specific permission.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {"type": "string", "description": "The ID of the user receiving the exception."},
                        "permission_id": {"type": "string",
                                          "description": "The ID of the specific permission being granted."},
                        "justification": {"type": "string",
                                          "description": "The business reason for the emergency exception."},
                        "approved_by": {"type": "string",
                                        "description": "The ID of the manager approving the exception."},
                        "expires_at": {"type": "string",
                                       "description": "The timestamp when this exception will automatically expire."},
                        "timestamp": {"type": "string",
                                      "description": "The current timestamp for the creation and review record."}
                    },
                    "required": ["user_id", "permission_id", "justification", "approved_by", "expires_at", "timestamp"]
                }
            }
        }
