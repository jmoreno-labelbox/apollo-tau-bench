from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any

class SummarizeAbstract(Tool):
    """Utility for creating a summary of an article's abstract."""

    @staticmethod
    def invoke(data: dict[str, Any], article_id: Any = None) -> str:
        if not article_id:
            payload = {"error": "article_id is required."}
            out = json.dumps(payload)
            return out

        articles = data.get("articles", [])
        for article in articles:
            if article.get("article_id") == article_id:
                summary = f"The article '{article.get('title')}' discusses {article.get('topic')}. The abstract focuses on {article.get('abstract')}"
                payload = {"summary": summary}
                out = json.dumps(payload)
                return out
        payload = {"error": f"Article with ID '{article_id}' not found."}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SummarizeAbstract",
                "description": "Generates a brief summary of an article's abstract.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "article_id": {
                            "type": "string",
                            "description": "The unique ID of the article to summarize.",
                        }
                    },
                    "required": ["article_id"],
                },
            },
        }
