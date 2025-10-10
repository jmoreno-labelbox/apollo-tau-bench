# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class SummarizeArticleText(Tool):
    """Tool to get a summary of an article."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        article_id = kwargs.get('article_id')
        if not article_id:
            return json.dumps({"error": "article_id is required."})

        articles = list(data.get('articles', {}).values())
        for article in articles:
            if article.get('article_id') == article_id:
                # This is a mock summary tool. In a real system, this would involve NLP.
                # Here, we just return the abstract, or a truncated part of the full text.
                summary = article.get('abstract', 'No abstract available.')
                if 'full_text' in article and len(summary) < 20:
                    summary = article['full_text'][:200] + "..."
                return json.dumps({"article_id": article_id, "summary": summary})
        return json.dumps({"error": "Article not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "summarize_article_text",
                "description": "Provides a concise summary of a given article's content.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "article_id": {"type": "string", "description": "The ID of the article to summarize."}
                    },
                    "required": ["article_id"]
                }
            }
        }
