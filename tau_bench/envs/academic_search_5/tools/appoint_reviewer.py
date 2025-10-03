from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime
from typing import Any

class AppointReviewer(Tool):
    """Utility for designating a reviewer for a submission."""

    @staticmethod
    def invoke(data: dict[str, Any], submission_id: Any = None, reviewer_user_id: Any = None) -> str:
        if not submission_id or not reviewer_user_id:
            payload = {"error": "submission_id and reviewer_user_id are required."}
            out = json.dumps(payload)
            return out

        submissions = data.get("submissions", [])
        for submission in submissions:
            if submission.get("submission_id") == submission_id:
                if "assigned_reviewers" not in submission:
                    submission["assigned_reviewers"] = []
                if reviewer_user_id not in submission["assigned_reviewers"]:
                    submission["assigned_reviewers"].append(reviewer_user_id)
                    payload = {
                        "success": True,
                        "submission_id": submission_id,
                        "reviewer_id": reviewer_user_id,
                    }
                    out = json.dumps(payload)
                    return out
                else:
                    payload = {"error": "Reviewer already assigned to this submission."}
                    out = json.dumps(payload)
                    return out
        payload = {"error": "Submission not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AppointReviewer",
                "description": "Assigns a researcher to review a submission.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "submission_id": {
                            "type": "string",
                            "description": "The ID of the submission.",
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
