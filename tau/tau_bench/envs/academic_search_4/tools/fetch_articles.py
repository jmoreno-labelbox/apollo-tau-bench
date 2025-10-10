# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class FetchArticles(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        article_id = kwargs.get('article_id')
        topic = kwargs.get('topic')
        title = kwargs.get('title')
        year = kwargs.get('year')
        author_name = kwargs.get('author_name')

        articles: list = list(data.get('articles', {}).values())

        if article_id:
            for article in articles:
                if article.get('article_id') == article_id:
                    return json.dumps([article], indent=2) # Return list with one item for consistency
            return json.dumps([]) # Return empty list if not found

        results = []
        for article in articles:
            match = True
            if topic and topic.lower() not in article.get('topic', '').lower(): match = False
            if title and title.lower() not in article.get('title', '').lower(): match = False
            if author_name and author_name.lower() not in article.get('author_name', '').lower(): match = False
            if year and year != article.get('publication_year'): match = False
            if match: results.append(article)
        return json.dumps(results, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function","function": {"name": "fetch_articles","description": "Searches for academic articles by ID, topic, title, or publication year.","parameters": {"type": "object","properties": {"article_id": {"type": "string","description": "The unique ID of the article."}, "topic": {"type": "string","description": "A topic to search for (e.g., 'AI', 'Biology')."},"title": {"type": "string","description": "A keyword or phrase from the article title."},"year": {"type": "integer","description": "A specific publication year to filter by."}},"required": []}}}
