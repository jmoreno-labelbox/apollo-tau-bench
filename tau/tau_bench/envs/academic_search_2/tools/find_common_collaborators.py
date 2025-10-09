from tau_bench.envs.tool import Tool
import json
import uuid
from collections import Counter
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class FindCommonCollaborators(Tool):
    """Identifies shared collaborators between two authors."""

    @staticmethod
    def invoke(data: dict[str, Any], author1_name: Any = None, author2_name: Any = None) -> str:
        if not all([author1_name, author2_name]):
            payload = {"error": "author1_name and author2_name are required."}
            out = json.dumps(payload)
            return out
        articles1 = [
            a for a in data.get("articles", {}).values() if author1_name in a.get("authors", [])
        ]
        collaborators1 = {
            author
            for article in articles1
            for author in article.get("authors", [])
            if author != author1_name
        }
        articles2 = [
            a for a in data.get("articles", {}).values() if author2_name in a.get("authors", [])
        ]
        collaborators2 = {
            author
            for article in articles2
            for author in article.get("authors", [])
            if author != author2_name
        }
        common_collaborators = list(collaborators1.intersection(collaborators2))
        payload = {"common_collaborators": common_collaborators}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FindCommonCollaborators",
                "description": "Finds common collaborators between two authors.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "author1_name": {"type": "string"},
                        "author2_name": {"type": "string"},
                    },
                    "required": ["author1_name", "author2_name"],
                },
            },
        }
