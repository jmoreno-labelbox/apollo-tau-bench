# Copyright Sierra

import uuid
import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateReview(Tool):
    """Creates a new review for a submission."""
    @staticmethod
    def invoke(data: Dict[str, Any], content, recommendation, review_id_override, reviewer_user_id, submission_id) -> str:
        submission_id, reviewer_user_id, content, recommendation = submission_id, reviewer_user_id, content, recommendation
        if not all([submission_id, reviewer_user_id, content, recommendation]):
            return json.dumps({"error": "submission_id, reviewer_user_id, content, and recommendation are required."})

        new_review = {
            "review_id": review_id_override if review_id_override else f"rev_{uuid.uuid4().hex[:4]}",
            "submission_id": submission_id,
            "reviewer_user_id": reviewer_user_id,
            "review_content": content,
            "recommendation": recommendation,
            "review_date": "2025-06-24"
        }
        list(data.get('reviews', {}).values()).append(new_review)
        return json.dumps({"success": True, "review": new_review}, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "create_review", "description": "Creates a new review for a submission.", "parameters": {"type": "object", "properties": {"submission_id": {"type": "string"}, "reviewer_user_id": {"type": "string"}, "content": {"type": "string"}, "recommendation": {"type": "string"}, "review_id_override": {"type": "string"}}, "required": ["submission_id", "reviewer_user_id", "content", "recommendation"]}}}
