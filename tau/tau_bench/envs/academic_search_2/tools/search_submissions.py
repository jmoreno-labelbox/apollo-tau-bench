# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class SearchSubmissions(Tool):
    """Searches for submissions by submission_id, article_id, or by a specific review_id."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        submission_id, article_id, review_id = kwargs.get('submission_id'), kwargs.get('article_id'), kwargs.get('review_id')

        # Code from the previous SearchReviews utility.
        if review_id:
            reviews = list(data.get('reviews', {}).values())
            target_review = next((r for r in reviews if r.get('review_id') == review_id), None)
            if not target_review:
                return json.dumps([]) # Return an empty list if no review is found.

            # Retrieve the submission using the submission_id from the review.
            submission_id_from_review = target_review.get('submission_id')
            submissions = list(data.get('submissions', {}).values())
            results = [s for s in submissions if s.get('submission_id') == submission_id_from_review]

            if results:
                results[0]['review_details'] = target_review # Include the complete review object.
            return json.dumps(results, indent=2)

        if not submission_id and not article_id:
            return json.dumps(list(data.get('submissions', {}).values()), indent=2)

        submissions = list(data.get('submissions', {}).values())
        results = [
            s for s in submissions if
            (not submission_id or s.get('submission_id') == submission_id) and
            (not article_id or s.get('article_id') == article_id)
        ]
        return json.dumps(results, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "search_submissions",
                "description": "Searches for submissions by submission_id, article_id, or indirectly via a review_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "submission_id": {"type": "string"},
                        "article_id": {"type": "string"},
                        "review_id": {"type": "string", "description": "If provided, finds the submission associated with this review."}
                    }
                }
            }
        }
