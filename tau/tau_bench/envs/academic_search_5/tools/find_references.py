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

class FindReferences(Tool):
    """Utility for querying citations."""

    @staticmethod
    def invoke(data: dict[str, Any], article_id: Any = None, direction: Any = None) -> str:
        article_id = article_id
        direction = direction  #'to' or 'from'
        if not article_id:
            payload = {"error": "article_id is required."}
            out = json.dumps(payload)
            return out

        citations = data.get("citations", {}).values()
        results = []
        if direction.lower() == "to":
            #Locate articles that have CITED the specified article_id
            results = [c for c in citations.values() if c.get("referenced_paper_id") == article_id]
        elif direction.lower() == "from":
            #Identify articles that are CITED BY the specified article_id
            results = [c for c in citations.values() if c.get("source_article_id") == article_id]
        else:
            payload = {"error": "Invalid direction. Must be 'to' or 'from'."}
            out = json.dumps(payload)
            return out
        payload = results
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FindReferences",
                "description": "Searches for citations. Can find which articles cited a given article, or which articles a given article cited.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "article_id": {
                            "type": "string",
                            "description": "The ID of the article to search citations for.",
                        },
                        "direction": {
                            "type": "string",
                            "description": "Search direction: 'to' (who cited this article) or 'from' (who did this article cite). Defaults to 'to'.",
                        },
                    },
                    "required": ["article_id"],
                },
            },
        }
