# Sierra Copyright

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GenerateNewReview(Tool):
    """Tool to generate a new review entry for a submission."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        review_id = f"rev_{len(list(data.get('reviews', {}).values())) + 1:02d}"
        new_review = {
            "review_id": review_id,
            "submission_id": kwargs.get('submission_id'),
            "reviewer_user_id": kwargs.get('reviewer_user_id'),
            "score": kwargs.get('score'),
            "comments": kwargs.get('comments'),
            "review_date": datetime.now().strftime('%Y-%m-%d')
        }
        list(data.get('reviews', {}).values()).append(new_review)
        return json.dumps(new_review, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "generate_new_review", "description": "Generates a new review for a submission.", "parameters": {"type": "object", "properties": {
            "submission_id": {"type": "string", "description": "The ID of the submission to be reviewed."},
            "reviewer_user_id": {"type": "string", "description": "The ID of the reviewing user."},
            "score": {"type": "integer", "description": "The review score (1-10)."},
            "comments": {"type": "string", "description": "Detailed comments for the review."}
        }, "required": ["submission_id", "reviewer_user_id", "score", "comments"]}}}
