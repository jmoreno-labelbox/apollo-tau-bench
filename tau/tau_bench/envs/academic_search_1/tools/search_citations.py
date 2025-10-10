# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class SearchCitations(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        """
        Searches for citations related to a specific article.
        - The search direction ('to' or 'from') is required.
        - 'to': Finds all citations that point TO the article_id.
        - 'from': Finds all citations made BY the article_id.
        """
        article_id = kwargs.get('article_id')
        direction = kwargs.get('direction')

        if not all([article_id, direction]):
            return json.dumps({"error": "article_id and direction are required."})

        citations = list(data.get('citations', {}).values())
        results = []

        if direction.lower() == 'to':
            keyword = kwargs.get('context_keyword', '').lower()
            results = [
                c for c in citations
                if c.get('cited_article_id') == article_id and
                (not keyword or keyword in c.get('citation_context', '').lower())
            ]
        elif direction.lower() == 'from':
            results = [c for c in citations if c.get('source_article_id') == article_id]
        else:
            return json.dumps({"error": "Invalid direction. Must be 'to' or 'from'."})

        return json.dumps(results, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        """
        Returns the function schema to be used by the language model.
        """
        return {
            "type": "function",
            "function": {
                "name": "search_citations",
                "description": "Searches for citations from or to an article. Use direction 'to' to find citations that an article received or 'from' to find citations that an article made.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "article_id": {"type": "string", "description": "The ID of the article to search for citations."},
                        "direction": {"type": "string", "enum": ["to", "from"], "description": "The direction of the search: 'to' (for citations to the article) or 'from' (for citations from the article)."},
                        "context_keyword": {"type": "string", "description": "Optional. A keyword to search for in the citation context (only for 'to' direction)."}
                    },
                    "required": ["article_id", "direction"]
                }
            }
        }
