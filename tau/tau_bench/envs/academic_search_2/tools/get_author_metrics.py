# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetAuthorMetrics(Tool):
    """Gets multiple metrics for an author."""
    @staticmethod
    def invoke(data: Dict[str, Any], author_name) -> str:
        if not author_name:
            return json.dumps({"error": "author_name is required."})
        articles = [a for a in list(data.get('articles', {}).values()) if author_name in a.get('authors', [])]
        if not articles:
            return json.dumps({"total_publications": 0, "total_citations": 0, "h_index": 0})
        citations = list(data.get('citations', {}).values())
        total_citations = 0
        citation_counts = []
        for article in articles:
            count = len([c for c in citations if c.get('cited_article_id') == article['article_id']])
            total_citations += count
            citation_counts.append(count)
        citation_counts.sort(reverse=True)
        h_index = 0
        for i, count in enumerate(citation_counts):
            if count >= i + 1: h_index = i + 1
            else: break
        return json.dumps({"total_publications": len(articles), "total_citations": total_citations, "h_index": h_index}, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "get_author_metrics", "description": "Gets multiple metrics for an author.", "parameters": {"type": "object", "properties": {"author_name": {"type": "string"}}, "required": ["author_name"]}}}
