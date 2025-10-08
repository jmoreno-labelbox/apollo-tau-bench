from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime
from typing import Any

class ModifySubmissionStatus(Tool):
    """Utility for modifying the status of a submission."""

    @staticmethod
    def invoke(data: dict[str, Any], submission_id: Any = None, new_status: Any = None) -> str:
        if not submission_id or not new_status:
            payload = {"error": "submission_id and new_status are required."}
            out = json.dumps(payload)
            return out

        submissions = data.get("submissions", [])
        for submission in submissions:
            if submission.get("submission_id") == submission_id:
                submission["status"] = new_status
                payload = {
                    "success": True,
                    "submission_id": submission_id,
                    "new_status": new_status,
                }
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
                "name": "ModifySubmissionStatus",
                "description": "Updates the status of a submission (e.g., 'under_review', 'accepted', 'rejected').",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "submission_id": {
                            "type": "string",
                            "description": "The ID of the submission to update.",
                        },
                        "new_status": {
                            "type": "string",
                            "description": "The new status for the submission.",
                        },
                    },
                    "required": ["submission_id", "new_status"],
                },
            },
        }
