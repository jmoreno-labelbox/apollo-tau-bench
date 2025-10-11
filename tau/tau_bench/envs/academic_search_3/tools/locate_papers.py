# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class LocatePapers(Tool):
    """Tool to search for academic articles by topic, title, or year."""
    @staticmethod
    def invoke(data: Dict[str, Any], article_id, title, topic, year) -> str:
        topic,title,year = topic,title,year
        articles: list = list(data.get('articles', {}).values())
        results = []
        for article in articles:
            match = True
            if article_id and article_id != article.get('article_id'): match = False
            if topic and topic.lower() not in article.get('topic', '').lower(): match = False
            if title and title.lower() not in article.get('title', '').lower(): match = False
            if year and year != article.get('publication_year'): match = False
            if match: results.append(article)
        return json.dumps(results, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function","function": {"name": "locate_papers","description": "Searches for academic articles by ID, topic, title, or publication year.","parameters": {"type": "object","properties": {"article_id": {"type": "string","description": "The unique ID of the article."}, "topic": {"type": "string","description": "A topic to search for (e.g., 'AI', 'Biology')."},"title": {"type": "string","description": "A keyword or phrase from the article title."},"year": {"type": "integer","description": "A specific publication year to filter by."}},"required": []}}}
