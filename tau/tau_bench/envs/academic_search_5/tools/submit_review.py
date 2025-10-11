# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class SubmitReview(Tool):
    """Tool to create a new review for a submission."""
    @staticmethod
    def invoke(data: Dict[str, Any], recommendation, review_content, reviewer_user_id, submission_id) -> str:

        if not all([submission_id, reviewer_user_id, review_content, recommendation]):
            return json.dumps({"error": "submission_id, reviewer_user_id, review_content, and recommendation are required."})

        new_review = {
            "review_id": f"rev_{uuid.uuid4().hex[:4]}",
            "submission_id": submission_id,
            "reviewer_user_id": reviewer_user_id,
            "review_content": review_content,
            "recommendation": recommendation,
            "review_date": datetime.now().strftime('%Y-%m-%d')
        }
        data['reviews'].append(new_review)
        return json.dumps({"success": True, "review": new_review})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "submit_review",
                "description": "Creates a new review for a submission.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "submission_id": {"type": "string", "description": "The ID of the submission being reviewed."},
                        "reviewer_user_id": {"type": "string", "description": "The user ID of the reviewer."},
                        "review_content": {"type": "string", "description": "The text content of the review."},
                        "recommendation": {"type": "string", "description": "The recommendation (e.g., 'accept', 'minor_revisions')."}
                    },
                    "required": ["submission_id", "reviewer_user_id", "review_content", "recommendation"]
                }
            }
        }
