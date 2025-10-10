# Copyright © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class AppointReviewer(Tool):
    """Tool to assign a reviewer to a submission."""
    @staticmethod
    def invoke(data: Dict[str, Any], reviewer_user_id, submission_id) -> str:
        if not submission_id or not reviewer_user_id:
            return json.dumps({"error": "submission_id and reviewer_user_id are required."})

        submissions = list(data.get('submissions', {}).values())
        for submission in submissions:
            if submission.get('submission_id') == submission_id:
                if 'assigned_reviewers' not in submission:
                    submission['assigned_reviewers'] = []
                if reviewer_user_id not in submission['assigned_reviewers']:
                    submission['assigned_reviewers'].append(reviewer_user_id)
                    return json.dumps({"success": True, "submission_id": submission_id, "reviewer_id": reviewer_user_id})
                else:
                    return json.dumps({"error": "Reviewer already assigned to this submission."})
        return json.dumps({"error": "Submission not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "appoint_reviewer",
                "description": "Assigns a researcher to review a submission.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "submission_id": {"type": "string", "description": "The ID of the submission."},
                        "reviewer_user_id": {"type": "string", "description": "The user ID of the reviewer to assign."}
                    },
                    "required": ["submission_id", "reviewer_user_id"]
                }
            }
        }
