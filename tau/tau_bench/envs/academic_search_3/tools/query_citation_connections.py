# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class QueryCitationConnections(Tool):
    """Tool to search for citations related to an article."""
    @staticmethod
    def invoke(data: Dict[str, Any], cited_article_id, source_article_id, direction = 'from') -> str:
        citations = list(data.get('citations', {}).values())
        results = []

        if direction == 'from' and 'source_article_id' in kwargs:
            source_id = source_article_id
            results = [c for c in citations if c.get('source_article_id') == source_id]

        elif direction == 'to' and 'cited_article_id' in kwargs:
            cited_id = cited_article_id
            results = [c for c in citations if c.get('cited_article_id') == cited_id]

        return json.dumps(results, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "query_citation_connections", "description": "Searches for citations, either from a source article or to a cited article.", "parameters": {"type": "object", "properties": {
            "source_article_id": {"type": "string", "description": "The ID of the article that made the citation."},
            "cited_article_id": {"type": "string", "description": "The ID of the article that received the citation."},
            "direction": {"type": "string", "enum": ["from", "to"], "description": "The direction of the citation search."}
        }, "required": ["direction"]}}}
