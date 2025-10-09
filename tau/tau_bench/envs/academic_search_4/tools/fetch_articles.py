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

class FetchArticles(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], *, article_id: Any = None, topic: Any = None, title: Any = None, year: Any = None, author_name: Any = None) -> str:
        articles: list = data.get("articles", {}).values()

        if article_id:
            for article in articles.values():
                if article.get("article_id") == article_id:
                    payload = [article]
                    out = json.dumps(
                        payload, indent=2
                    )
                    return out
            payload = []
            out = json.dumps(payload)
            return out

        results = []
        for article in articles.values():
            match = True
            if topic and topic.lower() not in article.get("topic", "").lower():
                match = False
            if title and title.lower() not in article.get("title", "").lower():
                match = False
            if (
                author_name
                and author_name.lower() not in article.get("author_name", "").lower()
            ):
                match = False
            if year and year != article.get("publication_year"):
                match = False
            if match:
                results.append(article)
        payload = results
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FetchArticles",
                "description": "Searches for academic articles by ID, topic, title, or publication year.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "article_id": {
                            "type": "string",
                            "description": "The unique ID of the article.",
                        },
                        "topic": {
                            "type": "string",
                            "description": "A topic to search for (e.g., 'AI', 'Biology').",
                        },
                        "title": {
                            "type": "string",
                            "description": "A keyword or phrase from the article title.",
                        },
                        "year": {
                            "type": "integer",
                            "description": "A specific publication year to filter by.",
                        },
                    },
                    "required": [],
                },
            },
        }
