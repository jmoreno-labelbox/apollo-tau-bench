from tau_bench.envs.tool import Tool
import json
import re
import uuid
from collections import Counter
from datetime import datetime
from typing import Any

class PostNewReview(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], submission_id: Any = None, reviewer_user_id: Any = None, recommendation: Any = None, comments: Any = None) -> str:
        if not all([submission_id, reviewer_user_id, recommendation, comments]):
            payload = {
                "error": "submission_id, reviewer_user_id, recommendation, and comments are required."
            }
            out = json.dumps(payload)
            return out

        new_review = {
            "review_id": f"rev_{uuid.uuid4().hex[:4]}",
            "submission_id": submission_id,
            "reviewer_user_id": reviewer_user_id,
            "recommendation": recommendation,
            "review_content": comments,
            "review_date": datetime.now().strftime("%Y-%m-%d"),
        }
        if "reviews" not in data:
            data["reviews"] = []
        data["reviews"].append(new_review)
        payload = {"success": True, "review": new_review}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "PostNewReview",
                "description": "Posts a new peer review for a submission.",
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
                        "recommendation": {
                            "type": "string",
                            "description": "The recommendation (e.g., 'accept', 'minor_revisions', 'reject').",
                        },
                        "comments": {
                            "type": "string",
                            "description": "The detailed comments of the review.",
                        },
                    },
                    "required": [
                        "submission_id",
                        "reviewer_user_id",
                        "recommendation",
                        "comments",
                    ],
                },
            },
        }
