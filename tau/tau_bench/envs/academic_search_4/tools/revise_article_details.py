from tau_bench.envs.tool import Tool
import json
import re
import uuid
from collections import Counter
from datetime import datetime
from typing import Any

class ReviseArticleDetails(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], *, article_id: Any = None, title: str = None, abstract: str = None, topic: str = None, status: str = None) -> str:
        article_id = article_id
        if not article_id:
            payload = {"error": "article_id is required."}
            out = json.dumps(payload)
            return out

        article = next(
            (a for a in data.get("articles", []) if a.get("article_id") == article_id),
            None,
        )
        if not article:
            payload = {"error": f"Article with ID '{article_id}' not found."}
            out = json.dumps(payload)
            return out

        updatable_fields = {"title": title, "abstract": abstract, "topic": topic, "status": status}
        for key, value in updatable_fields.items():
            if value is not None:
                article[key] = value
        payload = {"success": True, "article": article}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ReviseArticleDetails",
                "description": "Revises details of an existing article, such as its abstract or status.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "article_id": {
                            "type": "string",
                            "description": "The ID of the article to revise.",
                        },
                        "title": {
                            "type": "string",
                            "description": "The new title for the article.",
                        },
                        "abstract": {
                            "type": "string",
                            "description": "The new abstract for the article.",
                        },
                        "topic": {
                            "type": "string",
                            "description": "The new topic for the article.",
                        },
                        "status": {
                            "type": "string",
                            "description": "The new status for the article.",
                        },
                    },
                    "required": ["article_id"],
                },
            },
        }
