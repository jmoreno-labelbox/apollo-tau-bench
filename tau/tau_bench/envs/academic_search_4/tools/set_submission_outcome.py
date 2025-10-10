# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class SetSubmissionOutcome(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], new_status, submission_id) -> str:

        if not all([submission_id, new_status]):
            return json.dumps({"error": "submission_id and new_status are required."})

        submissions = list(data.get('submissions', {}).values())
        for sub in submissions:
            if sub.get('submission_id') == submission_id:
                sub['status'] = new_status
                return json.dumps({"success": True, "submission": sub})
        return json.dumps({"error": f"Submission with ID '{submission_id}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "set_submission_outcome", "description": "Sets the outcome or status for a submission (e.g., 'accepted', 'rejected').", "parameters": {"type": "object", "properties": {"submission_id": {"type": "string", "description": "The ID of the submission to update."}, "new_status": {"type": "string", "description": "The new status to set for the submission."}}, "required": ["submission_id", "new_status"]}}}
