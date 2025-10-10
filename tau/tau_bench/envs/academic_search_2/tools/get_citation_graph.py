# Copyright by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetCitationGraph(Tool):
    """
    Gets the citation graph for a specific article.
    If a second article ID is provided via 'compare_with_article_id', it finds the common citations between the two.
    """
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        article_id = kwargs.get('article_id')
        compare_with_article_id = kwargs.get('compare_with_article_id')

        if not article_id:
            return json.dumps({"error": "article_id is required."})

        citations = list(data.get('citations', {}).values())

        # Implementation from the previous FindCommonCitations utility.
        if compare_with_article_id:
            cites1 = {c['cited_article_id'] for c in citations if c.get('source_article_id') == article_id}
            cites2 = {c['cited_article_id'] for c in citations if c.get('source_article_id') == compare_with_article_id}
            common_citations = list(cites1.intersection(cites2))
            return json.dumps({"article1_id": article_id, "article2_id": compare_with_article_id, "common_citations": common_citations}, indent=2)

        # Initial implementation of GetCitationGraph
        else:
            cited_by = [c['source_article_id'] for c in citations if c.get('cited_article_id') == article_id]
            cites = [c['cited_article_id'] for c in citations if c.get('source_article_id') == article_id]
            result = {"article_id": article_id, "cited_by": cited_by, "cites": cites}
            return json.dumps(result, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_citation_graph",
                "description": "Gets the citation graph for an article, or finds common citations between two articles.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "article_id": {"type": "string"},
                        "compare_with_article_id": {"type": "string", "description": "If provided, finds common articles cited by both this article and the main article_id."}
                    },
                    "required": ["article_id"]
                }
            }
        }
