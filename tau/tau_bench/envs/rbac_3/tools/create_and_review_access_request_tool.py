# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateAndReviewAccessRequestTool(Tool):
    """
    create_and_review_access_request
    Create an access request and immediately review it per policy (with audit). If approved, assign role.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        request_id = kwargs.get("request_id")
        user_id = kwargs.get("user_id")
        resource_id = kwargs.get("resource_id")
        requested_role_id = kwargs.get("requested_role_id")
        justification = kwargs.get("justification") or ""
        reviewer_id = kwargs.get("reviewer_id")

        missing = [
            k
            for k in [
                "request_id",
                "user_id",
                "resource_id",
                "requested_role_id",
                "reviewer_id",
            ]
            if not kwargs.get(k)
        ]
        if missing:
            return json.dumps(
                {"error": f"Missing required: {', '.join(missing)}"}, indent=2
            )

        # Create if absent
        json.loads(
            CreateAccessRequestTool.invoke(
                data,
                request_id=request_id,
                user_id=user_id,
                resource_id=resource_id,
                requested_role_id=requested_role_id,
                justification=justification,
                submitted_at=_HARD_TS,
            )
        )

        # Process end-to-end using existing composite
        return ProcessAccessRequestE2ETool.invoke(
            data, request_id=request_id, reviewer_id=reviewer_id
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_and_review_access_request",
                "description": (
                    "Create an access request and process it end-to-end per policy."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "request_id": {"type": "string"},
                        "user_id": {"type": "string"},
                        "resource_id": {"type": "string"},
                        "requested_role_id": {"type": "string"},
                        "justification": {"type": "string"},
                        "reviewer_id": {"type": "string"},
                    },
                    "required": [
                        "request_id",
                        "user_id",
                        "resource_id",
                        "requested_role_id",
                        "reviewer_id",
                    ],
                },
            },
        }
