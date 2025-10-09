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

class CreateArticle(Tool):
    """Establishes a new article record."""

    @staticmethod
    def invoke(data: dict[str, Any], *, title: Any = None, authors: Any = None, topic: Any = None, publication_year: Any = None, article_id_override: Any = None, abstract: str = "...") -> str:
        #Retrieve parameters for the new article
        title = title
        authors = authors
        topic = topic
        publication_year = publication_year
        article_id_override = article_id_override

        if not all([title, authors, topic, publication_year]):
            payload = {"error": "title, authors, topic, and publication_year are required."}
            out = json.dumps(
                payload)
            return out

        new_article = {
            "article_id": (
                article_id_override
                if article_id_override
                else f"art_{uuid.uuid4().hex[:4]}"
            ),
            "title": title,
            "authors": authors,
            "publication_year": publication_year,
            "topic": topic,
            "abstract": abstract,
            "status": "new",
        }
        data.get("articles", []).append(new_article)
        payload = {"success": True, "article": new_article}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateArticle",
                "description": "Creates a new article record.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "title": {"type": "string"},
                        "authors": {"type": "array", "items": {"type": "string"}},
                        "topic": {"type": "string"},
                        "publication_year": {"type": "integer"},
                        "abstract": {"type": "string"},
                        "article_id_override": {"type": "string"},
                    },
                    "required": ["title", "authors", "topic", "publication_year"],
                },
            },
        }
