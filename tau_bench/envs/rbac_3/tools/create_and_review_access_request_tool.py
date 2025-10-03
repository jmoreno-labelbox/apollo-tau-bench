from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any
from datetime import datetime, timedelta

class CreateAndReviewAccessRequestTool(Tool):
    """
    create_and_review_access_request
    Generate an access request and promptly review it according to policy (with audit). If authorized, assign role.
    """

    @staticmethod
    def invoke(
        data: dict[str, Any],
        request_id: str = None,
        user_id: str = None,
        resource_id: str = None,
        requested_role_id: str = None,
        justification: str = "",
        reviewer_id: str = None
    ) -> str:
        pass
        missing = [
            k
            for k in [
                "request_id",
                "user_id",
                "resource_id",
                "requested_role_id",
                "reviewer_id",
            ]
            if not locals().get(k)
        ]
        if missing:
            payload = {"error": f"Missing required: {', '.join(missing)}"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        # Establish if not present
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

        # Execute end-to-end with the current composite
        return ProcessAccessRequestE2ETool.invoke(
            data, request_id=request_id, reviewer_id=reviewer_id
        )
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "createAndReviewAccessRequest",
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
