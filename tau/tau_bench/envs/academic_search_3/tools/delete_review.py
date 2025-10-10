# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class DeleteReview(Tool):
    """Tool to delete a review record."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        review_id = kwargs.get('review_id')
        reviews = list(data.get('reviews', {}).values())
        original_count = len(reviews)
        data['reviews'] = [r for r in reviews if r.get('review_id') != review_id]
        if len(data['reviews']) < original_count:
            return json.dumps({"status": "success", "review_id": review_id, "message": "Review deleted."})
        else:
            return json.dumps({"error": f"Review with ID {review_id} not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "delete_review", "description": "Deletes a specific review record by its ID.", "parameters": {"type": "object", "properties": {
            "review_id": {"type": "string", "description": "The unique ID of the review to delete."}
        }, "required": ["review_id"]}}}
