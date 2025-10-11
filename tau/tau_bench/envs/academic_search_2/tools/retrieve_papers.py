# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class RetrievePapers(Tool):
    """Searches for academic articles by ID, topic, title, year, or author name."""
    @staticmethod
    def invoke(data: Dict[str, Any], article_id, author_name, title, topic, year) -> str:
        articles: list = list(data.get('articles', {}).values())

        if article_id:
            for article in articles:
                if article.get('article_id') == article_id:
                    return json.dumps([article], indent=2)
            return json.dumps([])

        topic, title, year, author_name = topic, title, year, author_name

        results = [
            a for a in articles if
            (not topic or topic.lower() in a.get('topic', '').lower()) and
            (not title or title.lower() in a.get('title', '').lower()) and
            (not year or year == a.get('publication_year')) and
            (not author_name or any(author_name.lower() in author.lower() for author in a.get('authors', [])))
        ]
        return json.dumps(results, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "retrieve_papers", "description": "Searches for academic articles by ID, topic, title, publication year, or author name.", "parameters": {"type": "object", "properties": {"article_id": {"type": "string"}, "topic": {"type": "string"}, "title": {"type": "string"}, "year": {"type": "integer"}, "author_name": {"type": "string"}}}}}
