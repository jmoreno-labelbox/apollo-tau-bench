# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class SearchArticles(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], abstract_keyword, article_id, author_name, full_text_keyword, title, topic, year) -> str:

        articles = list(data.get('articles', {}).values())

        if article_id:
            for article in articles:
                if article.get('article_id') == article_id:
                    return json.dumps([article], indent=2)
            return json.dumps({"error": f"Article with ID '{article_id}' not found."})

        if not any([title, topic, year, author_name, abstract_keyword, full_text_keyword]):
            return json.dumps(articles, indent=2)

        results = [
            a for a in articles
            if (not title or title.lower() in a.get('title', '').lower()) and
               (not topic or topic.lower() in a.get('topic', '').lower()) and
               (not year or year == a.get('publication_year')) and
               (not author_name or any(author_name.lower() in author.lower() for author in a.get('authors', []))) and
               (not abstract_keyword or abstract_keyword.lower() in a.get('abstract', '').lower()) and
               (not full_text_keyword or full_text_keyword.lower() in a.get('full_text', '').lower())
        ]
        return json.dumps(results, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        """
        Returns the function schema to be used by the language model.
        """
        return {
            "type": "function",
            "function": {
                "name": "search_articles",
                "description": "Searches for academic articles by ID, title, topic, year, author, or keywords in the abstract or full text. If an article_id is provided, it returns the details of that specific article.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "article_id": {"type": "string", "description": "The ID of the article to retrieve details for."},
                        "title": {"type": "string", "description": "A keyword or phrase from the article title."},
                        "topic": {"type": "string", "description": "A topic to search for (e.g., 'IA', 'Biology')."},
                        "year": {"type": "integer", "description": "A specific publication year to filter by."},
                        "author_name": {"type": "string", "description": "The name of an author to search for."},
                        "abstract_keyword": {"type": "string", "description": "A keyword to search for within the article's abstract."},
                        "full_text_keyword": {"type": "string", "description": "A keyword to search for within the article's full text."}
                    }
                }
            }
        }
