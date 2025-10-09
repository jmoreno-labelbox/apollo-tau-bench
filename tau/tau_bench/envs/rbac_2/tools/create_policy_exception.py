from tau_bench.envs.tool import Tool
import json
from datetime import datetime, timezone
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class CreatePolicyException(Tool):
    """Establish a new policy exception to provide emergency access based on a particular permission."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        timestamp: str = None,
        user_id: str = None,
        permission_id: str = None,
        approved_by: str = None,
        expires_on: str = None,
        justification: str = None
    ) -> str:
        try:
            policy_exceptions = data.get("policy_exceptions", {}).values()
        except:
            policy_exceptions = []

        existing_ids = [
            int(item["exception_id"].replace("PE-", ""))
            for item in policy_exceptions.values() if item.get("exception_id", "").startswith("PE-")
        ]
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
            "status": "ACTIVE",
        }

        data["policy_exceptions"][new_exception["policy_exception_id"]] = new_exception
        data["policy_exceptions"] = policy_exceptions
        payload = {
            "message": "Policy exception created successfully.",
            "exception_details": new_exception,
        }
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreatePolicyException",
                "description": "Creates a policy exception to grant temporary, emergency access for a specific permission.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "The ID of the user receiving the exception.",
                        },
                        "permission_id": {
                            "type": "string",
                            "description": "The ID of the specific permission being granted.",
                        },
                        "justification": {
                            "type": "string",
                            "description": "The business reason for the emergency exception.",
                        },
                        "approved_by": {
                            "type": "string",
                            "description": "The ID of the manager approving the exception.",
                        },
                        "expires_at": {
                            "type": "string",
                            "description": "The timestamp when this exception will automatically expire.",
                        },
                        "timestamp": {
                            "type": "string",
                            "description": "The current timestamp for the creation and review record.",
                        },
                    },
                    "required": [
                        "user_id",
                        "permission_id",
                        "justification",
                        "approved_by",
                        "expires_at",
                        "timestamp",
                    ],
                },
            },
        }
