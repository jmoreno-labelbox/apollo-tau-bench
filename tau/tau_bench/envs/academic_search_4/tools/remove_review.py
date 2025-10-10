# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class RemoveReview(Tool):
    """Deletes a review record from the system."""
    @staticmethod
    def invoke(data: Dict[str, Any], review_id) -> str:
        if not review_id:
            return json.dumps({"error": "review_id is required."})

        reviews = list(data.get('reviews', {}).values())
        original_count = len(reviews)
        # Reminder: In an actual database, this would perform a direct deletion. Instead, we are filtering the list.
        data['reviews'] = [r for r in reviews if r.get('review_id') != review_id]

        if len(data['reviews']) < original_count:
            return json.dumps({"success": True, "message": f"Review {review_id} has been deleted."})
        else:
            return json.dumps({"error": f"Review with ID '{review_id}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "remove_review", "description": "Deletes a specific review by its ID.", "parameters": {"type": "object", "properties": {"review_id": {"type": "string", "description": "The ID of the review to delete."}}, "required": ["review_id"]}}}
