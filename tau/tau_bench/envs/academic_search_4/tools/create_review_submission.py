from tau_bench.envs.tool import Tool
import json
import re
import uuid
from collections import Counter
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class CreateReviewSubmission(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], author_user_id: Any = None, submission_id_override: Any = None, article_id: Any = None) -> str:
        author_user_id, article_id = author_user_id, article_id
        submission_id_override = submission_id_override

        if not author_user_id or not article_id:
            payload = {"error": "author_user_id and article_id are required."}
            out = json.dumps(payload)
            return out
        if not any(u["person_id"] == author_user_id for u in data.get("users", {}).values():
            payload = {"error": f"Author with ID '{author_user_id}' not found."}
            out = json.dumps(payload)
            return out
        if not any(a.get("article_id") == article_id or a.get("paper_id") == article_id for a in data.get("articles", {}).values():
            payload = {"error": f"Article with ID '{article_id}' not found."}
            out = json.dumps(payload)
            return out

        new_submission_id = (
            submission_id_override
            if submission_id_override
            else f"sub_{uuid.uuid4().hex[:4]}"
        )

        new_submission = {
            "submission_id": new_submission_id,
            "article_id": article_id,
            "author_user_id": author_user_id,
            "submission_date": datetime.now().strftime("%Y-%m-%d"),
            "status": "submitted",
            "assigned_reviewers": [],
        }
        if "submissions" not in data:
            data["submissions"] = []
        data["submissions"][submission_id] = new_submission
        payload = {"success": True, "submission": new_submission}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateReviewSubmission",
                "description": "Submits an author's article to the peer review system.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "author_user_id": {
                            "type": "string",
                            "description": "The user ID of the author.",
                        },
                        "article_id": {
                            "type": "string",
                            "description": "The ID of the article being submitted.",
                        },
                        "submission_id_override": {
                            "type": "string",
                            "description": "Optional. A specific ID to assign to the new submission.",
                        },
                    },
                    "required": ["author_user_id", "article_id"],
                },
            },
        }
