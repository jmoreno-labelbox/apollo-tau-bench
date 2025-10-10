# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetReviewBySubmission(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        submission_id = kwargs.get('submission_id')
        if not submission_id:
            return json.dumps({"error": "submission_id is required."})

        reviews = list(data.get('reviews', {}).values())
        for review in reviews:
            if review.get('submission_id') == submission_id:
                return json.dumps(review, indent=2)

        return json.dumps({"error": f"No review found for submission_id '{submission_id}'."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "get_review_by_submission", "description": "Retrieves a review's details using the ID of the submission.", "parameters": {"type": "object", "properties": {"submission_id": {"type": "string", "description": "The unique ID of the submission to find the review for."}}, "required": ["submission_id"]}}}
