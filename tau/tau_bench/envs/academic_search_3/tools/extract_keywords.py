# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ExtractKeywords(Tool):
    """Tool to extract keywords from an article's abstract."""
    @staticmethod
    def invoke(data: Dict[str, Any], article_id) -> str:
        if not article_id:
            return json.dumps({"error": "article_id is required."})

        articles = list(data.get('articles', {}).values())
        for article in articles:
            if article.get('article_id') == article_id:
                abstract = article.get('abstract', '').lower()
                potential_keywords = ["transformer", "crispr-cas9", "biomarkers", "dark matter", "quantum computing", "gene therapy"]
                found_keywords = [kw for kw in potential_keywords if kw in abstract]
                return json.dumps(found_keywords)

        return json.dumps({"error": f"Article with ID '{article_id}' not found."})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function","function": {"name": "extract_keywords","description": "Extracts a list of pre-defined keywords from an article's abstract.","parameters": {"type": "object","properties": {"article_id": {"type": "string","description": "The unique ID of the article to extract keywords from."}},"required": ["article_id"]}}}
