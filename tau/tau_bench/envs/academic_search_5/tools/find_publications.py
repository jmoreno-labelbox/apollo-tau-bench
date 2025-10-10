# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class FindPublications(Tool):
    """Tool to search for articles based on various criteria."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        title = kwargs.get('title')
        author_name = kwargs.get('author_name')
        topic = kwargs.get('topic')
        publication_year = kwargs.get('publication_year')
        article_id = kwargs.get('article_id')

        if not any([title, author_name, topic, publication_year, article_id]):
            return json.dumps({"error": "At least one search parameter is required."})

        articles = list(data.get('articles', {}).values())
        results = []
        for article in articles:
            title_match = not title or title.lower() in article.get('title', '').lower()
            author_match = not author_name or any(author_name.lower() in author.lower() for author in article.get('authors', []))
            topic_match = not topic or topic.lower() == article.get('topic', '').lower()
            year_match = not publication_year or str(publication_year) == str(article.get('publication_year'))
            id_match = not article_id or article_id == article.get('article_id')

            if all([title_match, author_match, topic_match, year_match, id_match]):
                results.append(article)
        return json.dumps(results, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "find_publications",
                "description": "Searches for articles by title, author, topic, or publication year.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "title": {"type": "string", "description": "The title or a keyword from the title of the article."},
                        "author_name": {"type": "string", "description": "The name of one of the authors."},
                        "topic": {"type": "string", "description": "The main topic of the article (e.g., 'AI', 'Biomedicine')."},
                        "publication_year": {"type": "integer", "description": "The year the article was published."},
                        "article_id": {"type": "string", "description": "The exact ID of the article."}
                    }
                }
            }
        }
