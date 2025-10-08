from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime
from typing import Any

class SearchCitations(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], article_id: Any = None, direction: Any = None, context_keyword: Any = None) -> str:
        """
        Looks for citations associated with a particular article.
        - The direction of the search ('to' or 'from') is necessary.
        - 'to': Locates all citations that reference the article_id.
        - 'from': Locates all citations authored by the article_id.
        """
        if not all([article_id, direction]):
            payload = {"error": "article_id and direction are required."}
            out = json.dumps(payload)
            return out

        citations = data.get("citations", [])
        results = []

        if direction.lower() == "to":
            keyword = context_keyword.lower() if context_keyword else None
            results = [
                c
                for c in citations
                if c.get("referenced_paper_id") == article_id
                and (not keyword or keyword in c.get("citation_context", "").lower())
            ]
        elif direction.lower() == "from":
            results = [c for c in citations if c.get("source_article_id") == article_id]
        else:
            payload = {"error": "Invalid direction. Must be 'to' or 'from'."}
            out = json.dumps(payload)
            return out
        payload = results
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        """
        Supplies the function schema for the language model's application.
        """
        pass
        return {
            "type": "function",
            "function": {
                "name": "SearchCitations",
                "description": "Searches for citations from or to an article. Use direction 'to' to find citations that an article received or 'from' to find citations that an article made.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "article_id": {
                            "type": "string",
                            "description": "The ID of the article to search for citations.",
                        },
                        "direction": {
                            "type": "string",
                            "enum": ["to", "from"],
                            "description": "The direction of the search: 'to' (for citations to the article) or 'from' (for citations from the article).",
                        },
                        "context_keyword": {
                            "type": "string",
                            "description": "Optional. A keyword to search for in the citation context (only for 'to' direction).",
                        },
                    },
                    "required": ["article_id", "direction"],
                },
            },
        }
