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
        return list(db.values())
    return db

class IdentifyPotentialReviewers(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], article_id: Any = None, exclude_user_ids: Any = None) -> str:
        if not article_id:
            payload = {"error": "article_id is required."}
            out = json.dumps(payload)
            return out

        articles = data.get("articles", [])
        target_article = next(
            (a for a in articles if a.get("article_id") == article_id), None
        )
        if not target_article:
            payload = {"error": f"Article with ID '{article_id}' not found."}
            out = json.dumps(payload)
            return out

        article_topic = target_article.get("topic")
        if not article_topic:
            payload = {"error": f"Article with ID '{article_id}' has no topic specified."}
            out = json.dumps(payload)
            return out

        users = data.get("users", [])
        potential_reviewers = [
            user
            for user in users
            if user.get("research_field") == article_topic
            and user.get("person_id") not in exclude_user_ids
        ]
        payload = potential_reviewers
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "IdentifyPotentialReviewers",
                "description": "Identifies potential reviewers for an article based on matching research fields.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "article_id": {
                            "type": "string",
                            "description": "The ID of the article needing reviewers.",
                        },
                        "exclude_user_ids": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "A list of user IDs to exclude from the suggestions (e.g., the authors).",
                        },
                    },
                    "required": ["article_id"],
                },
            },
        }
