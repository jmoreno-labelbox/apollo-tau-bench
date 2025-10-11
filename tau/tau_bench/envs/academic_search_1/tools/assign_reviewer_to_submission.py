# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class AssignReviewerToSubmission(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], reviewer_user_id, submission_id) -> str:
        if not all([submission_id, reviewer_user_id]):
            return json.dumps({"error": "submission_id and reviewer_user_id are required."})

        for sub in list(data.get('submissions', {}).values()):
            if sub['submission_id'] == submission_id:
                if reviewer_user_id not in sub['assigned_reviewers']:
                    sub['assigned_reviewers'].append(reviewer_user_id)
                return json.dumps({"success": True, "submission": sub})

        return json.dumps({"error": f"Submission with ID '{submission_id}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "assign_reviewer_to_submission", "description": "Assigns a reviewer to a submission.", "parameters": {"type": "object", "properties": {"submission_id": {"type": "string", "description": "The ID of the submission to update."}, "reviewer_user_id": {"type": "string", "description": "The user ID of the reviewer to assign."}}, "required": ["submission_id", "reviewer_user_id"]}}}
