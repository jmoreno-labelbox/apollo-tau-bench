from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime
from typing import Any

class GetReviewsForSubmission(Tool):
    """Utility for fetching all reviews related to a particular submission."""

    @staticmethod
    def invoke(data: dict[str, Any], *, submission_id: Any = None) -> str:
        if not submission_id:
            payload = {"error": "submission_id is required."}
            out = json.dumps(payload)
            return out

        reviews = data.get("reviews", [])
        submission_reviews = [
            review for review in reviews if review.get("submission_id") == submission_id
        ]
        payload = submission_reviews
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetReviewsForSubmission",
                "description": "Gets all reviews associated with a single submission.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "submission_id": {
                            "type": "string",
                            "description": "The ID of the submission to get reviews for.",
                        }
                    },
                    "required": ["submission_id"],
                },
            },
        }
