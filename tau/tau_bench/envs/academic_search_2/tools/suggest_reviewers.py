# Sierra Copyright

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class SuggestReviewers(Tool):
    """Suggests potential reviewers for an article, with an option to exclude certain authors."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        article_id = kwargs.get('article_id')
        exclude_authors = kwargs.get('exclude_authors', [])
        if not article_id:
            return json.dumps({"error": "article_id is required."})
        article = next((a for a in list(data.get('articles', {}).values()) if a.get('article_id') == article_id), None)
        if not article:
            return json.dumps({"error": "Article not found."})
        topic = article.get('topic')
        authors = [a.get('authors') for a in list(data.get('articles', {}).values()) if a.get('topic') == topic and a.get('article_id') != article_id]
        authors = [author for sublist in authors for author in sublist]
        authors = [author for author in dict.fromkeys(authors) if author not in exclude_authors]
        return json.dumps({"suggested_reviewers": authors}, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "suggest_reviewers", "description": "Suggests potential reviewers for an article.", "parameters": {"type": "object", "properties": {"article_id": {"type": "string"}, "exclude_authors": {"type": "array", "items": {"type": "string"}}}, "required": ["article_id"]}}}
