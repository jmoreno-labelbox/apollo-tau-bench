from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any

class GenerateNewReview(Tool):
    """Utility for creating a new review entry for a submission."""

    @staticmethod
    def invoke(data: dict[str, Any], submission_id: str = None, reviewer_user_id: str = None, score: int = None, comments: str = None) -> str:
        review_id = f"rev_{len(data.get('reviews', [])) + 1:02d}"
        new_review = {
            "review_id": review_id,
            "submission_id": submission_id,
            "reviewer_user_id": reviewer_user_id,
            "score": score,
            "comments": comments,
            "review_date": datetime.now().strftime("%Y-%m-%d"),
        }
        data.get("reviews", []).append(new_review)
        payload = new_review
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GenerateNewReview",
                "description": "Generates a new review for a submission.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "submission_id": {
                            "type": "string",
                            "description": "The ID of the submission to be reviewed.",
                        },
                        "reviewer_user_id": {
                            "type": "string",
                            "description": "The ID of the reviewing user.",
                        },
                        "score": {
                            "type": "integer",
                            "description": "The review score (1-10).",
                        },
                        "comments": {
                            "type": "string",
                            "description": "Detailed comments for the review.",
                        },
                    },
                    "required": [
                        "submission_id",
                        "reviewer_user_id",
                        "score",
                        "comments",
                    ],
                },
            },
        }
