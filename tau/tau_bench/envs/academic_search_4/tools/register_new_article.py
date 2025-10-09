from tau_bench.envs.tool import Tool
import json
import re
import uuid
from collections import Counter
from datetime import datetime
from typing import Any

class RegisterNewArticle(Tool):
    """Records a new manuscript for an article within the system."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        *,
        title: Any = None,
        authors: Any = None,
        topic: Any = None,
        abstract: Any = None,
        article_id_override: Any = None,
        full_text: str = ""
    ) -> str:
        title = title
        authors = authors
        topic = topic
        abstract = abstract
        article_id_override = article_id_override

        if not all([title, authors, topic, abstract]):
            payload = {"error": "title, authors, topic, and abstract are required."}
            out = json.dumps(payload)
            return out

        new_article_id = (
            article_id_override
            if article_id_override
            else f"art_{uuid.uuid4().hex[:4]}"
        )

        new_article = {
            "article_id": new_article_id,
            "title": title,
            "authors": authors,
            "publication_year": datetime.now().year,
            "topic": topic,
            "abstract": abstract,
            "status": "draft",
            "full_text": full_text,
        }
        if "articles" not in data:
            data["articles"] = []
        data["articles"][article_id] = new_article
        payload = {"success": True, "article": new_article}
        out = json.dumps(payload)
        return out
    
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "RegisterNewArticle",
                "description": "Registers a new article manuscript in the system.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "title": {"type": "string"},
                        "authors": {"type": "array", "items": {"type": "string"}},
                        "topic": {"type": "string"},
                        "abstract": {"type": "string"},
                        "article_id_override": {
                            "type": "string",
                            "description": "Optional. A specific ID to assign to the new article for predictable referencing.",
                        },
                    },
                    "required": ["title", "authors", "topic", "abstract"],
                },
            },
        }
