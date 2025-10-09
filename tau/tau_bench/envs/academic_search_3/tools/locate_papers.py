from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class LocatePapers(Tool):
    """Utility for finding academic papers based on topic, title, or year."""

    @staticmethod
    def invoke(
        data: dict[str, Any], 
        topic: str = None, 
        title: str = None, 
        year: int = None, 
        article_id: str = None
    ) -> str:
        articles: list = data.get("articles", [])
        results = []
        for article in articles:
            match = True
            if article_id and article_id != article.get("article_id"):
                match = False
            if topic and topic.lower() not in article.get("topic", "").lower():
                match = False
            if title and title.lower() not in article.get("title", "").lower():
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
                "name": "LocatePapers",
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
