from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class RegisterArticleRecord(Tool):
    """Utility for generating a new article record."""

    @staticmethod
    def invoke(data: dict[str, Any], title: str, authors: list = None, topic: str = None, abstract: str = None) -> str:
        if authors is None:
            authors = []
        articles = data.get("articles", [])
        new_article = {
            "article_id": f"art_{len(articles) + 1:02d}",
            "title": title,
            "authors": authors,
            "publication_year": datetime.now().year,
            "topic": topic,
            "abstract": abstract,
            "status": "draft",
        }
        articles.append(new_article)
        payload = new_article
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "RegisterArticleRecord",
                "description": "Creates a new draft article record.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "title": {
                            "type": "string",
                            "description": "The title of the article.",
                        },
                        "authors": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "A list of author names.",
                        },
                        "topic": {
                            "type": "string",
                            "description": "The primary topic of the article.",
                        },
                        "abstract": {
                            "type": "string",
                            "description": "The abstract of the article.",
                        },
                    },
                    "required": ["title", "authors", "topic", "abstract"],
                },
            },
        }
