# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class FindReferences(Tool):
    """Tool to search for citations."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        article_id = kwargs.get('article_id')
        direction = kwargs.get('direction', 'to')  # 'to' or 'from'
        if not article_id:
            return json.dumps({"error": "article_id is required."})

        citations = list(data.get('citations', {}).values())
        results = []
        if direction.lower() == 'to':
            # Find articles that CITED the given article_id
            results = [c for c in citations if c.get('cited_article_id') == article_id]
        elif direction.lower() == 'from':
            # Find articles that ARE CITED BY the given article_id
            results = [c for c in citations if c.get('source_article_id') == article_id]
        else:
            return json.dumps({"error": "Invalid direction. Must be 'to' or 'from'."})
        return json.dumps(results, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "find_references",
                "description": "Searches for citations. Can find which articles cited a given article, or which articles a given article cited.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "article_id": {"type": "string", "description": "The ID of the article to search citations for."},
                        "direction": {"type": "string", "description": "Search direction: 'to' (who cited this article) or 'from' (who did this article cite). Defaults to 'to'."}
                    },
                    "required": ["article_id"]
                }
            }
        }
