# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class FindCitations(Tool):
    """Finds all articles that cite a given article."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        article_id = kwargs.get('article_id')
        if not article_id:
            return json.dumps({"error": "article_id is required."})

        citations = list(data.get('citations', {}).values())
        citing_articles = [c.get('source_article_id') for c in citations if c.get('cited_article_id') == article_id]

        return json.dumps(citing_articles, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "find_citations", "description": "Finds all articles that cite a given article ID.", "parameters": {"type": "object", "properties": {"article_id": {"type": "string", "description": "The ID of the article to find citations for."}}, "required": ["article_id"]}}}
