from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class QueryCitationConnections(Tool):
    """Utility for finding citations associated with an article."""

    @staticmethod
    def invoke(data: dict[str, Any], direction: Any = None, source_article_id: str = None, cited_article_id: str = None) -> str:
        citations = data.get("citations", {}).values()
        results = []

        if direction == "from" and source_article_id is not None:
            source_id = source_article_id
            results = [c for c in citations.values() if c.get("source_article_id") == source_id]

        elif direction == "to" and cited_article_id is not None:
            cited_id = cited_article_id
            results = [c for c in citations.values() if c.get("referenced_paper_id") == cited_id]
        payload = results
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "QueryCitationConnections",
                "description": "Searches for citations, either from a source article or to a cited article.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "source_article_id": {
                            "type": "string",
                            "description": "The ID of the article that made the citation.",
                        },
                        "cited_article_id": {
                            "type": "string",
                            "description": "The ID of the article that received the citation.",
                        },
                        "direction": {
                            "type": "string",
                            "enum": ["from", "to"],
                            "description": "The direction of the citation search.",
                        },
                    },
                    "required": ["direction"],
                },
            },
        }
