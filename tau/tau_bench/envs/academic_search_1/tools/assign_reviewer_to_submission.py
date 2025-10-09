from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime
from typing import Any

class AssignReviewerToSubmission(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], submission_id: Any = None, reviewer_user_id: Any = None) -> str:
        if not all([submission_id, reviewer_user_id]):
            payload = {"error": "submission_id and reviewer_user_id are required."}
            out = json.dumps(payload)
            return out

        for sub in data.get("submissions", []):
            if sub["proposal_id"] == submission_id:
                if reviewer_user_id not in sub["allocated_evaluators"]:
                    sub["allocated_evaluators"].append(reviewer_user_id)
                payload = {"success": True, "submission": sub}
                out = json.dumps(payload)
                return out
        payload = {"error": f"Submission with ID '{submission_id}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AssignReviewerToSubmission",
                "description": "Assigns a reviewer to a submission.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "submission_id": {
                            "type": "string",
                            "description": "The ID of the submission to update.",
                        },
                        "reviewer_user_id": {
                            "type": "string",
                            "description": "The user ID of the reviewer to assign.",
                        },
                    },
                    "required": ["submission_id", "reviewer_user_id"],
                },
            },
        }
