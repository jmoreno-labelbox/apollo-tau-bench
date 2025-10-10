# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateArticle(Tool):
    """Creates a new article record."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        # Retrieve parameters for the new article.
        title = kwargs.get('title')
        authors = kwargs.get('authors')
        topic = kwargs.get('topic')
        publication_year = kwargs.get('publication_year')
        article_id_override = kwargs.get('article_id_override')

        if not all([title, authors, topic, publication_year]):
            return json.dumps({"error": "title, authors, topic, and publication_year are required."})

        new_article = {
            "article_id": article_id_override if article_id_override else f"art_{uuid.uuid4().hex[:4]}",
            "title": title,
            "authors": authors,
            "publication_year": publication_year,
            "topic": topic,
            "abstract": kwargs.get('abstract', '...'),
            "status": "new"
        }
        list(data.get('articles', {}).values()).append(new_article)
        return json.dumps({"success": True, "article": new_article}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "create_article", "description": "Creates a new article record.", "parameters": {"type": "object", "properties": {"title": {"type": "string"}, "authors": {"type": "array", "items": {"type": "string"}}, "topic": {"type": "string"}, "publication_year": {"type": "integer"}, "abstract": {"type": "string"}, "article_id_override": {"type": "string"}}, "required": ["title", "authors", "topic", "publication_year"]}}}
