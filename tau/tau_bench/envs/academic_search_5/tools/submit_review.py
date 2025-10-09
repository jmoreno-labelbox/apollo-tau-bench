from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime
from typing import Any

class SubmitReview(Tool):
    """Utility for generating a new review for a submission."""

    @staticmethod
    def invoke(data: dict[str, Any], submission_id: Any = None, reviewer_user_id: Any = None, review_content: Any = None, recommendation: Any = None) -> str:
        if not all([submission_id, reviewer_user_id, review_content, recommendation]):
            payload = {
                "error": "submission_id, reviewer_user_id, review_content, and recommendation are required."
            }
            out = json.dumps(payload)
            return out

        new_review = {
            "review_id": f"rev_{uuid.uuid4().hex[:4]}",
            "submission_id": submission_id,
            "reviewer_user_id": reviewer_user_id,
            "review_content": review_content,
            "recommendation": recommendation,
            "review_date": datetime.now().strftime("%Y-%m-%d"),
        }
        data["reviews"][review_id] = new_review
        payload = {"success": True, "review": new_review}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SubmitReview",
                "description": "Creates a new review for a submission.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "submission_id": {
                            "type": "string",
                            "description": "The ID of the submission being reviewed.",
                        },
                        "reviewer_user_id": {
                            "type": "string",
                            "description": "The user ID of the reviewer.",
                        },
                        "review_content": {
                            "type": "string",
                            "description": "The text content of the review.",
                        },
                        "recommendation": {
                            "type": "string",
                            "description": "The recommendation (e.g., 'accept', 'minor_revisions').",
                        },
                    },
                    "required": [
                        "submission_id",
                        "reviewer_user_id",
                        "review_content",
                        "recommendation",
                    ],
                },
            },
        }
