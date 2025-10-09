from tau_bench.envs.tool import Tool
import json
import uuid
from collections import Counter
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class CreateReview(Tool):
    """Generates a new review for a submission."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        submission_id: str = None,
        reviewer_user_id: str = None,
        content: str = None,
        recommendation: str = None,
        review_id_override: Any = None
    ) -> str:
        if not all([submission_id, reviewer_user_id, content, recommendation]):
            payload = {
                "error": "submission_id, reviewer_user_id, content, and recommendation are required."
            }
            out = json.dumps(payload)
            return out

        new_review = {
            "review_id": (
                review_id_override
                if review_id_override
                else f"rev_{uuid.uuid4().hex[:4]}"
            ),
            "submission_id": submission_id,
            "reviewer_user_id": reviewer_user_id,
            "review_content": content,
            "recommendation": recommendation,
            "review_date": "2025-06-24",
        }
        data["reviews"][new_review["review_id"]] = new_review
        payload = {"success": True, "review": new_review}
        out = json.dumps(payload, indent=2)
        return out
    
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateReview",
                "description": "Creates a new review for a submission.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "submission_id": {"type": "string"},
                        "reviewer_user_id": {"type": "string"},
                        "content": {"type": "string"},
                        "recommendation": {"type": "string"},
                        "review_id_override": {"type": "string"},
                    },
                    "required": [
                        "submission_id",
                        "reviewer_user_id",
                        "content",
                        "recommendation",
                    ],
                },
            },
        }
