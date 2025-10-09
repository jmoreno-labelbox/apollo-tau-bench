from tau_bench.envs.tool import Tool
import json
import uuid
from collections import Counter
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class SuggestReviewers(Tool):
    """Recommends possible reviewers for an article, allowing for the exclusion of specific authors."""

    @staticmethod
    def invoke(data: dict[str, Any], article_id: Any = None, exclude_authors: Any = None) -> str:
        article_id = article_id
        exclude_authors = exclude_authors
        if not article_id:
            payload = {"error": "article_id is required."}
            out = json.dumps(payload)
            return out
        article = next(
            (a for a in data.get("articles", []) if a.get("article_id") == article_id),
            None,
        )
        if not article:
            payload = {"error": "Article not found."}
            out = json.dumps(payload)
            return out
        topic = article.get("topic")
        authors = [
            a.get("authors")
            for a in data.get("articles", [])
            if a.get("topic") == topic and a.get("article_id") != article_id
        ]
        authors = [author for sublist in authors for author in sublist]
        authors = [
            author for author in dict.fromkeys(authors) if author not in exclude_authors
        ]
        payload = {"suggested_reviewers": authors}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SuggestReviewers",
                "description": "Suggests potential reviewers for an article.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "article_id": {"type": "string"},
                        "exclude_authors": {
                            "type": "array",
                            "items": {"type": "string"},
                        },
                    },
                    "required": ["article_id"],
                },
            },
        }
