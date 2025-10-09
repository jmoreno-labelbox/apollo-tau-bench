from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class SubmitArticleForReview(Tool):
    """Utility for submitting a new article."""

    @staticmethod
    def invoke(data: dict[str, Any], article_id: str = None, author_user_id: str = None) -> str:
        submissions = data.get("submissions", [])
        new_submission = {
            "submission_id": f"sub_{len(submissions) + 1:02d}",
            "article_id": article_id,
            "author_user_id": author_user_id,
            "submission_date": datetime.now().strftime("%Y-%m-%d"),
            "status": "submitted",
            "assigned_reviewers": [],
        }
        submissions.append(new_submission)
        payload = new_submission
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SubmitArticleForReview",
                "description": "Creates a new article submission for the review process.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "article_id": {
                            "type": "string",
                            "description": "The ID of the article being submitted.",
                        },
                        "author_user_id": {
                            "type": "string",
                            "description": "The ID of the submitting author.",
                        },
                    },
                    "required": ["article_id", "author_user_id"],
                },
            },
        }
