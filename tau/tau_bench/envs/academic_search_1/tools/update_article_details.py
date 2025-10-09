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

class UpdateArticleDetails(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], article_id: str = None, new_topic: str = None, new_status: str = None) -> str:
        if not article_id or (not new_topic and not new_status):
            payload = {"error": "article_id and either new_topic or new_status are required."}
            out = json.dumps(payload)
            return out
        for article in data.get("articles", []):
            if article["paper_id"] == article_id:
                if new_topic:
                    article["subject"] = new_topic
                if new_status:
                    article["state"] = new_status
                payload = {"success": True, "article": article}
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
                "name": "UpdateArticleDetails",
                "description": "Updates the details (e.g., topic, status) of an article.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "article_id": {
                            "type": "string",
                            "description": "The ID of the article to update.",
                        },
                        "new_topic": {
                            "type": "string",
                            "description": "The new topic for the article.",
                        },
                        "new_status": {
                            "type": "string",
                            "description": "The new status for the article (e.g., 'new', 'processing', 'archived').",
                        },
                    },
                    "required": ["article_id"],
                },
            },
        }
