# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class SearchReviews(Tool):
    """Tool to search for reviews by submission and reviewer."""
    @staticmethod
    def invoke(data: Dict[str, Any], reviewer_user_id, submission_id) -> str:
        reviews = list(data.get('reviews', {}).values())
        results = [r for r in reviews if r.get('submission_id') == submission_id and r.get('reviewer_user_id') == reviewer_user_id]
        return json.dumps(results, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "search_reviews", "description": "Searches for specific reviews by submission and reviewer ID.", "parameters": {"type": "object", "properties": {
            "submission_id": {"type": "string", "description": "The submission's ID."},
            "reviewer_user_id": {"type": "string", "description": "The reviewer's ID."}
        }, "required": ["submission_id", "reviewer_user_id"]}}}
