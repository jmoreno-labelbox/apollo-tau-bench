# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ReviseArticleDetails(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        article_id = kwargs.get('article_id')
        if not article_id:
            return json.dumps({"error": "article_id is required."})

        article = next((a for a in list(data.get('articles', {}).values()) if a.get('article_id') == article_id), None)
        if not article:
            return json.dumps({"error": f"Article with ID '{article_id}' not found."})

        updatable_fields = ['title', 'abstract', 'topic', 'status']
        for key, value in kwargs.items():
            if key in updatable_fields:
                article[key] = value

        return json.dumps({"success": True, "article": article})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "revise_article_details", "description": "Revises details of an existing article, such as its abstract or status.", "parameters": {"type": "object", "properties": {"article_id": {"type": "string", "description": "The ID of the article to revise."}, "title": {"type": "string", "description": "The new title for the article."}, "abstract": {"type": "string", "description": "The new abstract for the article."}, "topic": {"type": "string", "description": "The new topic for the article."}, "status": {"type": "string", "description": "The new status for the article."}}, "required": ["article_id"]}}}
