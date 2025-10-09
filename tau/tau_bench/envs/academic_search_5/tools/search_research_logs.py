from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class SearchResearchLogs(Tool):
    """Utility for querying research logs."""

    @staticmethod
    def invoke(data: dict[str, Any], researcher_id: Any = None, article_id: Any = None) -> str:
        researcher_id = researcher_id
        article_id = article_id

        if not researcher_id and not article_id:
            payload = {"error": "Either researcher_id or article_id is required."}
            out = json.dumps(
                payload)
            return out

        logs = data.get("research_logs", {}).values()
        results = [
            log
            for log in logs.values() if (not researcher_id or log.get("researcher_id") == researcher_id)
            and (not article_id or log.get("article_id") == article_id)
        ]
        payload = results
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SearchResearchLogs",
                "description": "Searches research logs by researcher or article.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "researcher_id": {
                            "type": "string",
                            "description": "The user ID of the researcher.",
                        },
                        "article_id": {
                            "type": "string",
                            "description": "The ID of the article.",
                        },
                    },
                },
            },
        }
