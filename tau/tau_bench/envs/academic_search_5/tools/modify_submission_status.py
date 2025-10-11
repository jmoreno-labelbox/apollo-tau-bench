# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ModifySubmissionStatus(Tool):
    """Tool to update the status of a submission."""
    @staticmethod
    def invoke(data: Dict[str, Any], new_status, submission_id) -> str:
        if not submission_id or not new_status:
            return json.dumps({"error": "submission_id and new_status are required."})

        submissions = list(data.get('submissions', {}).values())
        for submission in submissions:
            if submission.get('submission_id') == submission_id:
                submission['status'] = new_status
                return json.dumps({"success": True, "submission_id": submission_id, "new_status": new_status})
        return json.dumps({"error": "Submission not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "modify_submission_status",
                "description": "Updates the status of a submission (e.g., 'under_review', 'accepted', 'rejected').",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "submission_id": {"type": "string", "description": "The ID of the submission to update."},
                        "new_status": {"type": "string", "description": "The new status for the submission."}
                    },
                    "required": ["submission_id", "new_status"]
                }
            }
        }
