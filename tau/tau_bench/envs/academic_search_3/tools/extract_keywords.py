from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class ExtractKeywords(Tool):
    """Utility for retrieving keywords from an article's abstract."""

    @staticmethod
    def invoke(data: dict[str, Any], article_id: Any = None) -> str:
        if not article_id:
            payload = {"error": "article_id is required."}
            out = json.dumps(payload)
            return out

        articles = data.get("articles", [])
        for article in articles:
            if article.get("article_id") == article_id:
                abstract = article.get("abstract", "").lower()
                potential_keywords = [
                    "transformer",
                    "crispr-cas9",
                    "biomarkers",
                    "dark matter",
                    "quantum computing",
                    "gene therapy",
                ]
                found_keywords = [kw for kw in potential_keywords if kw in abstract]
                payload = found_keywords
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
                "name": "ExtractKeywords",
                "description": "Extracts a list of pre-defined keywords from an article's abstract.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "article_id": {
                            "type": "string",
                            "description": "The unique ID of the article to extract keywords from.",
                        }
                    },
                    "required": ["article_id"],
                },
            },
        }
