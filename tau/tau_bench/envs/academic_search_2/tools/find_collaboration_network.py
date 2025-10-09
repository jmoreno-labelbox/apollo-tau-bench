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

class FindCollaborationNetwork(Tool):
    """
    Identifies the collaboration network for a specified author.
    Can be limited to examine only a particular list of possible collaborators.
    """

    @staticmethod
    def invoke(data: dict[str, Any], author_name: Any = None, authors_to_check: Any = None) -> str:
        author_name = author_name
        authors_to_check = authors_to_check
        if not author_name:
            payload = {"error": "author_name is required."}
            out = json.dumps(payload)
            return out

        # Retrieve all articles authored by the primary author
        articles = [
            a for a in data.get("articles", {}).values() if author_name in a.get("authors", [])
        ]

        # Tally all collaborators associated with those articles
        all_collaborators = Counter()
        for article in articles:
            for author in article.get("authors", []):
                if author != author_name:
                    all_collaborators[author] += 1

        # If a designated list of authors is given, refine the results
        if authors_to_check:
            final_counts = {
                author: all_collaborators.get(author, 0) for author in authors_to_check
            }
            payload = final_counts
            out = json.dumps(payload, indent=2)
            return out
        payload = dict(all_collaborators)
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FindCollaborationNetwork",
                "description": "Finds the collaboration network for an author, optionally checking against a specific list of names.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "author_name": {"type": "string"},
                        "authors_to_check": {
                            "type": "array",
                            "items": {"type": "string"},
                        },
                    },
                    "required": ["author_name"],
                },
            },
        }
