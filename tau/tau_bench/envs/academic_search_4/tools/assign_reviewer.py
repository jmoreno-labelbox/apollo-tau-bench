# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class AssignReviewer(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], reviewer_user_id, submission_id, overwrite = False) -> str:

        submissions = list(data.get('submissions', {}).values())
        for sub in submissions:
            if sub['submission_id'] == submission_id:
                if overwrite:
                    sub['assigned_reviewers'] = [reviewer_user_id]
                else:
                    if reviewer_user_id not in sub['assigned_reviewers']:
                        sub['assigned_reviewers'].append(reviewer_user_id)

                sub['status'] = 'under_review'
                return json.dumps({"success": True, "submission": sub})
        return json.dumps({"error": f"Submission with ID '{submission_id}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function","function": {"name": "assign_reviewer","description": "Assigns a reviewer to an article submission, with an option to overwrite the existing list.","parameters": {"type": "object","properties": {"submission_id": {"type": "string", "description": "The ID of the submission."}, "reviewer_user_id": {"type": "string", "description": "The user ID of the person assigned to review."}, "overwrite": {"type": "boolean", "description": "If true, replaces the reviewer list. Defaults to false (append)."}},"required": ["submission_id", "reviewer_user_id"]}}}
