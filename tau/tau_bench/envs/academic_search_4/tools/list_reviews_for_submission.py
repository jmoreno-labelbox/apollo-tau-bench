# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ListReviewsForSubmission(Tool):
    """Lista todas as avaliações submetidas para uma submissão específica."""
    @staticmethod
    def invoke(data: Dict[str, Any], submission_id) -> str:
        if not submission_id:
            return json.dumps({"error": "submission_id is required."})

        reviews = list(data.get('reviews', {}).values())
        submission_reviews = [r for r in reviews if r.get('submission_id') == submission_id]

        return json.dumps(submission_reviews, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "list_reviews_for_submission", "description": "Lists all submitted reviews for a specific submission ID.", "parameters": {"type": "object", "properties": {"submission_id": {"type": "string", "description": "The ID of the submission to get reviews for."}}, "required": ["submission_id"]}}}
