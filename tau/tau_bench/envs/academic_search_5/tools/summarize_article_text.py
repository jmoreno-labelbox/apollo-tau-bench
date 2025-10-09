from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class SummarizeArticleText(Tool):
    """Utility for obtaining a summary of an article."""

    @staticmethod
    def invoke(data: dict[str, Any], article_id: Any = None) -> str:
        if not article_id:
            payload = {"error": "article_id is required."}
            out = json.dumps(payload)
            return out

        articles = data.get("articles", [])
        for article in articles:
            if article.get("article_id") == article_id:
                # This serves as a mock summary tool. In an actual system, it would utilize NLP.
                # In this case, we return only the abstract or a shortened version of the complete text.
                summary = article.get("abstract", "No abstract available.")
                if "full_text" in article and len(summary) < 20:
                    summary = article["full_text"][:200] + "..."
                payload = {"article_id": article_id, "summary": summary}
                out = json.dumps(payload)
                return out
        payload = {"error": "Article not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SummarizeArticleText",
                "description": "Provides a concise summary of a given article's content.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "article_id": {
                            "type": "string",
                            "description": "The ID of the article to summarize.",
                        }
                    },
                    "required": ["article_id"],
                },
            },
        }
