from tau_bench.envs.tool import Tool
import json
import uuid
from collections import Counter
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class UpdateArticleMetadata(Tool):
    """Modifies article metadata for designated fields."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        *,
        article_id: Any = None,
        title: str = None,
        authors: list[str] = None,
        publication_year: int = None,
        topic: str = None,
        abstract: str = None,
        status: str = None,
        keywords: list[str] = None
    ) -> str:
        article_id = article_id
        if not article_id:
            payload = {"error": "article_id is required."}
            out = json.dumps(payload)
            return out
        article = next(
            (a for a in data.get("articles", {}).values() if a.get("article_id") == article_id),
            None,
        )
        if not article:
            payload = {"error": "Article not found."}
            out = json.dumps(payload)
            return out

        updatable_fields = [
            "title",
            "authors",
            "publication_year",
            "topic",
            "abstract",
            "status",
            "keywords",
        ]
        updates = {
            "title": title,
            "authors": authors,
            "publication_year": publication_year,
            "topic": topic,
            "abstract": abstract,
            "status": status,
            "keywords": keywords,
        }
        for key, value in updates.items():
            if key in updatable_fields and value is not None:
                article[key] = value
        payload = {"success": True, "article": article}
        out = json.dumps(payload, indent=2)
        return out
    
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateArticleMetadata",
                "description": "Updates article metadata (e.g., topic, status, keywords).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "article_id": {"type": "string"},
                        "topic": {"type": "string"},
                        "status": {"type": "string"},
                        "keywords": {"type": "array", "items": {"type": "string"}},
                    },
                    "required": ["article_id"],
                },
            },
        }
