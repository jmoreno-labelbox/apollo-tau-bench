# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateSubmission(Tool):
    """Updates a submission's status or overwrites its list of reviewers."""
    @staticmethod
    def invoke(data: Dict[str, Any], status, submission_id, reviewers = []) -> str:
        if not submission_id:
            return json.dumps({"error": "submission_id is required."})

        submission = next((s for s in list(data.get('submissions', {}).values()) if s.get('submission_id') == submission_id), None)
        if not submission: return json.dumps({"error": "Submission not found."})

        if 'reviewers' in kwargs:
            provided_reviewers = reviewers
            users = list(data.get('users', {}).values())

            valid_reviewer_ids = []
            for reviewer_item in provided_reviewers:
                if any(u['user_id'] == reviewer_item for u in users):
                    valid_reviewer_ids.append(reviewer_item)
                else:
                    found_user = next((u for u in users if u['name'] == reviewer_item), None)
                    if found_user:
                        valid_reviewer_ids.append(found_user['user_id'])

            submission['assigned_reviewers'] = sorted(list(set(valid_reviewer_ids)))

        if 'status' in kwargs:
            submission['status'] = status

        return json.dumps({"success": True, "submission": submission}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "update_submission", "description": "Updates a submission's status or overwrites its list of reviewers.", "parameters": {"type": "object", "properties": {"submission_id": {"type": "string"}, "reviewers": {"type": "array", "items": {"type": "string", "description": "List of reviewer user_ids or names to assign."}}, "status": {"type": "string"}}, "required": ["submission_id"]}}}
