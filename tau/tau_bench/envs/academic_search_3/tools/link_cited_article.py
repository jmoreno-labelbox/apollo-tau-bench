# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class LinkCitedArticle(Tool):
    """Tool to create a new citation record between two articles."""
    @staticmethod
    def invoke(data: Dict[str, Any], cited_article_id, source_article_id, citation_context = 'Citation added for reference.') -> str:
        citations = list(data.get('citations', {}).values())
        new_citation_id = f"cit_{len(citations) + 1:02d}"
        new_citation = {
            "citation_id": new_citation_id,
            "source_article_id": source_article_id,
            "cited_article_id": cited_article_id,
            "citation_context": citation_context
        }
        citations.append(new_citation)
        return json.dumps(new_citation, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "link_cited_article", "description": "Creates a new citation record to link a source article to a cited article.", "parameters": {"type": "object", "properties": {
            "source_article_id": {"type": "string", "description": "The ID of the article making the citation."},
            "cited_article_id": {"type": "string", "description": "The ID of the article being cited."},
            "citation_context": {"type": "string", "description": "A brief description of the citation's context."}
        }, "required": ["source_article_id", "cited_article_id"]}}}
