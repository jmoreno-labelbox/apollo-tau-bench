from tau_bench.envs.tool import Tool
import json
import re
import uuid
from collections import Counter
from datetime import datetime
from typing import Any

class FindCitations(Tool):
    """Identifies all articles that reference a specified article."""

    @staticmethod
    def invoke(data: dict[str, Any], article_id: Any = None, citations: list = None) -> str:
        if not article_id:
            payload = {"error": "article_id is required."}
            out = json.dumps(payload)
            return out

        citations = citations or []
        citing_articles = [
            c.get("source_article_id")
            for c in citations
            if c.get("referenced_paper_id") == article_id
        ]
        payload = citing_articles
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FindCitations",
                "description": "Finds all articles that cite a given article ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "article_id": {
                            "type": "string",
                            "description": "The ID of the article to find citations for.",
                        }
                    },
                    "required": ["article_id"],
                },
            },
        }
