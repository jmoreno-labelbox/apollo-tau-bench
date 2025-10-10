# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class SummarizeAbstract(Tool):
    """Tool to generate a summary of an article's abstract."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        article_id = kwargs.get('article_id')
        if not article_id:
            return json.dumps({"error": "article_id is required."})

        articles = list(data.get('articles', {}).values())
        for article in articles:
            if article.get('article_id') == article_id:
                summary = f"The article '{article.get('title')}' discusses {article.get('topic')}. The abstract focuses on {article.get('abstract')}"
                return json.dumps({"summary": summary})

        return json.dumps({"error": f"Article with ID '{article_id}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function","function": {"name": "summarize_abstract","description": "Generates a brief summary of an article's abstract.","parameters": {"type": "object","properties": {"article_id": {"type": "string","description": "The unique ID of the article to summarize."}},"required": ["article_id"]}}}
