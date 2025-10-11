# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateCitation(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], cited_article_id, source_article_id, citation_context = 'No context provided.') -> str:
        context = citation_context
        if not all([source_article_id, cited_article_id]):
            return json.dumps({"error": "source_article_id and cited_article_id are required."})

        new_id = f"cit_{uuid.uuid4().hex[:4]}"
        new_citation = {
            "citation_id": new_id,
            "source_article_id": source_article_id,
            "cited_article_id": cited_article_id,
            "citation_context": context
        }
        data['citations'].append(new_citation)
        return json.dumps({"success": True, "citation": new_citation})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "create_citation", "description": "Creates a new citation, linking a source article to a cited article.", "parameters": {"type": "object", "properties": {"source_article_id": {"type": "string", "description": "The ID of the article making the citation."}, "cited_article_id": {"type": "string", "description": "The ID of the article being cited."}, "citation_context": {"type": "string", "description": "The sentence or context in which the citation is made."}}, "required": ["source_article_id", "cited_article_id"]}}}
