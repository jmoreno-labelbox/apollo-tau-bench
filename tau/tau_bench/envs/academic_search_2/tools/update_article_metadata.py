# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateArticleMetadata(Tool):
    """Updates article metadata for specified fields."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        article_id = kwargs.get('article_id')
        if not article_id:
            return json.dumps({"error": "article_id is required."})
        article = next((a for a in list(data.get('articles', {}).values()) if a.get('article_id') == article_id), None)
        if not article:
            return json.dumps({"error": "Article not found."})

        updatable_fields = ['title', 'authors', 'publication_year', 'topic', 'abstract', 'status', 'keywords']
        for key, value in kwargs.items():
            if key in updatable_fields and key != 'article_id':
                article[key] = value
        return json.dumps({"success": True, "article": article}, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "update_article_metadata", "description": "Updates article metadata (e.g., topic, status, keywords).", "parameters": {"type": "object", "properties": {"article_id": {"type": "string"}, "topic": {"type": "string"}, "status": {"type": "string"}, "keywords": {"type": "array", "items": {"type": "string"}}}, "required": ["article_id"]}}}
