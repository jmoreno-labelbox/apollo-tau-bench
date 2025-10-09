from tau_bench.envs.tool import Tool
import json
import uuid
from collections import Counter
from datetime import datetime
from typing import Any

class CreateSubmission(Tool):
    """Initiates a new article submission."""

    @staticmethod
    def invoke(data: dict[str, Any], article_id: Any = None, submission_id_override: Any = None, author_user_id: Any = None) -> str:
        if not all([article_id, author_user_id]):
            payload = {"error": "article_id and author_user_id are required."}
            out = json.dumps(payload)
            return out
        new_submission = {
            "submission_id": (
                submission_id_override
                if submission_id_override
                else f"sub_{uuid.uuid4().hex[:4]}"
            ),
            "article_id": article_id,
            "author_user_id": author_user_id,
            "submission_date": "2025-06-24",
            "status": "submitted",
            "assigned_reviewers": [],
        }
        data.get("submissions", []).append(new_submission)
        payload = {"success": True, "submission": new_submission}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateSubmission",
                "description": "Creates a new article submission.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "article_id": {"type": "string"},
                        "author_user_id": {"type": "string"},
                        "submission_id_override": {"type": "string"},
                    },
                    "required": ["article_id", "author_user_id"],
                },
            },
        }
