from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class SummarizeArticle(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], article_id: Any = None) -> str:
        """
        Locates an article using its ID and provides a summary of its complete text.
        The summary is created by pulling the first three sentences.
        """
        if not article_id:
            payload = {"error": "article_id is required."}
            out = json.dumps(payload)
            return out

        articles = data.get("articles", [])
        for article in articles:
            if article.get("paper_id") == article_id:
                full_text = article.get("complete_text")
                if not full_text:
                    payload = {
                        "error": f"Article with ID '{article_id}' has no full text to summarize."
                    }
                    out = json.dumps(payload)
                    return out

                # Basic summarization approach: extract the initial three sentences.
                sentences = full_text.split(".")
                summary = ". ".join(sentences[:3]).strip()
                if summary:
                    summary += "."
                payload = {"success": True, "article_id": article_id, "summary": summary}
                out = json.dumps(payload)
                return out
        payload = {"error": f"Article with ID '{article_id}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        """
        Delivers the function schema for the language model's application.
        """
        pass
        return {
            "type": "function",
            "function": {
                "name": "SummarizeArticle",
                "description": "Generates a concise summary of an article's full text using its ID.",
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
