# Copyright © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
import re


class GetArticleKeywords(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], article_id) -> str:
        if not article_id:
            return json.dumps({"error": "article_id is required."})

        article = next((a for a in list(data.get('articles', {}).values()) if a.get('article_id') == article_id), None)
        if not article or not article.get('abstract'):
            return json.dumps([])

        text = article.get('abstract', '').lower()
        words = re.findall(r'\b\w+\b', text)
        stop_words = {'a', 'an', 'the', 'in', 'of', 'for', 'is', 'on', 'and', 'to', 'with', 'by', 'as', 'its', 'we', 'this'}
        meaningful_words = [word for word in words if word not in stop_words and not word.isdigit()]

        top_keywords = [word for word, count in Counter(meaningful_words).most_common(5)]

        return json.dumps(top_keywords)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "get_article_keywords", "description": "Identifies potential keywords from an article's abstract based on word frequency.", "parameters": {"type": "object", "properties": {"article_id": {"type": "string", "description": "The ID of the article to extract keywords from."}}, "required": ["article_id"]}}}
