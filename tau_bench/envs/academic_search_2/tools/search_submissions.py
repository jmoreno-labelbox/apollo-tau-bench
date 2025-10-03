from tau_bench.envs.tool import Tool
import json
import uuid
from collections import Counter
from datetime import datetime
from typing import Any

class SearchSubmissions(Tool):
    """Finds submissions using submission_id, article_id, or a specific review_id."""

    @staticmethod
    def invoke(data: dict[str, Any], submission_id: str = None, article_id: str = None, review_id: str = None) -> str:
        # Functionality derived from the previous SearchReviews tool
        if review_id:
            reviews = data.get("reviews", [])
            target_review = next(
                (r for r in reviews if r.get("review_id") == review_id), None
            )
            if not target_review:
                payload = []
                out = json.dumps(payload)
                return out

            # Utilize the submission_id from the review to locate the submission
            submission_id_from_review = target_review.get("submission_id")
            submissions = data.get("submissions", [])
            results = [
                s
                for s in submissions
                if s.get("submission_id") == submission_id_from_review
            ]

            if results:
                results[0][
                    "review_details"
                ] = target_review  # Include the complete review object
            payload = results
            out = json.dumps(payload, indent=2)
            return out

        if not submission_id and not article_id:
            payload = data.get("submissions", [])
            out = json.dumps(payload, indent=2)
            return out

        submissions = data.get("submissions", [])
        results = [
            s
            for s in submissions
            if (not submission_id or s.get("submission_id") == submission_id)
            and (not article_id or s.get("article_id") == article_id)
        ]
        payload = results
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SearchSubmissions",
                "description": "Searches for submissions by submission_id, article_id, or indirectly via a review_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "submission_id": {"type": "string"},
                        "article_id": {"type": "string"},
                        "review_id": {
                            "type": "string",
                            "description": "If provided, finds the submission associated with this review.",
                        },
                    },
                },
            },
        }
