# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class AddCitation(Tool):
    """Adds a new citation."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        source_article_id, cited_article_id, context = kwargs.get('source_article_id'), kwargs.get('cited_article_id'), kwargs.get('context')
        if not all([source_article_id, cited_article_id]):
            return json.dumps({"error": "source_article_id and cited_article_id are required."})
        new_citation = {"citation_id": f"cit_{uuid.uuid4().hex[:4]}", "source_article_id": source_article_id, "cited_article_id": cited_article_id, "citation_context": context}
        list(data.get('citations', {}).values()).append(new_citation)
        return json.dumps({"success": True, "citation": new_citation}, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "add_citation", "description": "Adds a new citation.", "parameters": {"type": "object", "properties": {"source_article_id": {"type": "string"}, "cited_article_id": {"type": "string"}, "context": {"type": "string"}}, "required": ["source_article_id", "cited_article_id"]}}}
