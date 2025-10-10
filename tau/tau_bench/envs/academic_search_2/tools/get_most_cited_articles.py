# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetMostCitedArticles(Tool):
    """Tool to get a list of the most cited articles."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        citations = list(data.get('citations', {}).values())
        cited_ids = [c['cited_article_id'] for c in citations]
        citation_counts = Counter(cited_ids)
        sorted_articles = sorted(citation_counts.items(), key=lambda item: item[1], reverse=True)
        result = [{"article_id": article_id, "citation_count": count} for article_id, count in sorted_articles]
        return json.dumps(result, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function","function": {"name": "get_most_cited_articles","description": "Returns a list of articles sorted by how many times they have been cited.","parameters": {"type": "object", "properties": {}}}}
