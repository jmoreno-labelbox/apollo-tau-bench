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

class RetrievePapers(Tool):
    """Seeks academic articles using ID, subject, title, year, or author name."""

    @staticmethod
    def invoke(
        data: dict[str, Any], 
        *, 
        article_id: Any = None, 
        topic: str = None, 
        title: str = None, 
        year: int = None, 
        publication_year: int = None,
        author_name: str = None
    ) -> str:
        articles: list = data.get("articles", [])

        if article_id:
            for article in articles:
                if article.get("article_id") == article_id:
                    payload = [article]
                    out = json.dumps(payload, indent=2)
                    return out
            payload = []
            out = json.dumps(payload)
            return out

        # Use publication_year if provided, otherwise fall back to year
        search_year = publication_year if publication_year is not None else year
        
        results = [
            a
            for a in articles
            if (not topic or topic.lower() in a.get("topic", "").lower())
            and (not title or title.lower() in a.get("title", "").lower())
            and (not search_year or search_year == a.get("publication_year"))
            and (
                not author_name
                or any(
                    author_name.lower() in author.lower()
                    for author in a.get("authors", [])
                )
            )
        ]
        payload = results
        out = json.dumps(payload, indent=2)
        return out
    
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "RetrievePapers",
                "description": "Searches for academic articles by ID, topic, title, publication year, or author name.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "article_id": {"type": "string"},
                        "topic": {"type": "string"},
                        "title": {"type": "string"},
                        "year": {"type": "integer"},
                        "publication_year": {"type": "integer"},
                        "author_name": {"type": "string"},
                    },
                },
            },
        }
