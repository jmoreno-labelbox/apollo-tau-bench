# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateArticleDetails(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        article_id, new_topic, new_status = kwargs.get('article_id'), kwargs.get('new_topic'), kwargs.get('new_status')
        if not article_id or (not new_topic and not new_status):
            return json.dumps({"error": "article_id and either new_topic or new_status are required."})
        for article in list(data.get('articles', {}).values()):
            if article['article_id'] == article_id:
                if new_topic:
                    article['topic'] = new_topic
                if new_status:
                    article['status'] = new_status
                return json.dumps({"success": True, "article": article})
        return json.dumps({"error": f"Article with ID '{article_id}' not found."})
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function","function": {"name": "update_article_details","description": "Updates the details (e.g., topic, status) of an article.","parameters": {"type": "object","properties": {"article_id": {"type": "string","description": "The ID of the article to update."},"new_topic": {"type": "string","description": "The new topic for the article."},"new_status": {"type": "string","description": "The new status for the article (e.g., 'new', 'processing', 'archived')."}},"required": ["article_id"]}}}
