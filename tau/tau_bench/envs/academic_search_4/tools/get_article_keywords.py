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

class GetArticleKeywords(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], article_id: Any = None) -> str:
        if not article_id:
            payload = {"error": "article_id is required."}
            out = json.dumps(payload)
            return out

        article = next(
            (a for a in data.get("articles", {}).values() if a.get("article_id") == article_id),
            None,
        )
        if not article or not article.get("abstract"):
            payload = []
            out = json.dumps(payload)
            return out

        text = article.get("abstract", "").lower()
        words = re.findall(r"\b\w+\b", text)
        stop_words = {
            "a",
            "an",
            "the",
            "in",
            "of",
            "for",
            "is",
            "on",
            "and",
            "to",
            "with",
            "by",
            "as",
            "its",
            "we",
            "this",
        }
        meaningful_words = [
            word for word in words if word not in stop_words and not word.isdigit()
        ]

        top_keywords = [
            word for word, count in Counter(meaningful_words).most_common(5)
        ]
        payload = top_keywords
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetArticleKeywords",
                "description": "Identifies potential keywords from an article's abstract based on word frequency.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "article_id": {
                            "type": "string",
                            "description": "The ID of the article to extract keywords from.",
                        }
                    },
                    "required": ["article_id"],
                },
            },
        }
