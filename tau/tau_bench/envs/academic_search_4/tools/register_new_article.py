# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class RegisterNewArticle(Tool):
    """Registers a new article manuscript in the system."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        title = kwargs.get('title')
        authors = kwargs.get('authors')
        topic = kwargs.get('topic')
        abstract = kwargs.get('abstract')
        article_id_override = kwargs.get('article_id_override')

        if not all([title, authors, topic, abstract]):
            return json.dumps({"error": "title, authors, topic, and abstract are required."})

        new_article_id = article_id_override if article_id_override else f"art_{uuid.uuid4().hex[:4]}"

        new_article = {
            "article_id": new_article_id,
            "title": title,
            "authors": authors,
            "publication_year": datetime.now().year,
            "topic": topic,
            "abstract": abstract,
            "status": "draft",
            "full_text": kwargs.get('full_text', '')
        }
        data['articles'].append(new_article)
        return json.dumps({"success": True, "article": new_article})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "register_new_article", "description": "Registers a new article manuscript in the system.", "parameters": {"type": "object", "properties": {"title": {"type": "string"}, "authors": {"type": "array", "items": {"type": "string"}}, "topic": {"type": "string"}, "abstract": {"type": "string"}, "article_id_override": {"type": "string", "description": "Optional. A specific ID to assign to the new article for predictable referencing."}}, "required": ["title", "authors", "topic", "abstract"]}}}
