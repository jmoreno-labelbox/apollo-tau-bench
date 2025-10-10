# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class PostNewReview(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        submission_id = kwargs.get('submission_id')
        reviewer_user_id = kwargs.get('reviewer_user_id')
        recommendation = kwargs.get('recommendation')
        comments = kwargs.get('comments')

        if not all([submission_id, reviewer_user_id, recommendation, comments]):
            return json.dumps({"error": "submission_id, reviewer_user_id, recommendation, and comments are required."})

        new_review = {"review_id": f"rev_{uuid.uuid4().hex[:4]}", "submission_id": submission_id, "reviewer_user_id": reviewer_user_id, "recommendation": recommendation, "review_content": comments, "review_date": datetime.now().strftime('%Y-%m-%d')}
        data['reviews'].append(new_review)
        return json.dumps({"success": True, "review": new_review})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "post_new_review", "description": "Posts a new peer review for a submission.", "parameters": {"type": "object", "properties": {"submission_id": {"type": "string", "description": "The ID of the submission being reviewed."}, "reviewer_user_id": {"type": "string", "description": "The user ID of the reviewer."}, "recommendation": {"type": "string", "description": "The recommendation (e.g., 'accept', 'minor_revisions', 'reject')."}, "comments": {"type": "string", "description": "The detailed comments of the review."}}, "required": ["submission_id", "reviewer_user_id", "recommendation", "comments"]}}}
