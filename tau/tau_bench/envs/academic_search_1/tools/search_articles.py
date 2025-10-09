from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class SearchArticles(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        *,
        article_id: Any = None,
        title: Any = None,
        topic: Any = None,
        year: Any = None,
        author_name: Any = None,
        abstract_keyword: Any = None,
        full_text_keyword: Any = None
    ) -> str:
        articles = data.get("articles", {}).values()

        if article_id:
            for article in articles.values():
                if article.get("paper_id") == article_id:
                    payload = [article]
                    out = json.dumps(payload, indent=2)
                    return out
            payload = {"error": f"Article with ID '{article_id}' not found."}
            out = json.dumps(payload)
            return out

        if not any(
            [title, topic, year, author_name, abstract_keyword, full_text_keyword]
        ):
            payload = articles
            out = json.dumps(payload, indent=2)
            return out

        results = [
            a
            for a in articles.values() if (not title or title.lower() in a.get("heading", "").lower())
            and (not topic or topic.lower() in a.get("subject", "").lower())
            and (not year or year == a.get("release_year"))
            and (
                not author_name
                or any(
                    author_name.lower() in author.lower()
                    for author in a.get("writers", [])
                )
            )
            and (
                not abstract_keyword
                or abstract_keyword.lower() in a.get("summary", "").lower()
            )
            and (
                not full_text_keyword
                or full_text_keyword.lower() in a.get("complete_text", "").lower()
            )
        ]
        payload = results
        out = json.dumps(payload, indent=2)
        return out
    
    @staticmethod
    def get_info() -> dict[str, Any]:
        """
        Provides the function schema designated for the language model.
        """
        pass
        return {
            "type": "function",
            "function": {
                "name": "SearchArticles",
                "description": "Searches for academic articles by ID, title, topic, year, author, or keywords in the abstract or full text. If an article_id is provided, it returns the details of that specific article.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "article_id": {
                            "type": "string",
                            "description": "The ID of the article to retrieve details for.",
                        },
                        "title": {
                            "type": "string",
                            "description": "A keyword or phrase from the article title.",
                        },
                        "topic": {
                            "type": "string",
                            "description": "A topic to search for (e.g., 'IA', 'Biology').",
                        },
                        "year": {
                            "type": "integer",
                            "description": "A specific publication year to filter by.",
                        },
                        "author_name": {
                            "type": "string",
                            "description": "The name of an author to search for.",
                        },
                        "abstract_keyword": {
                            "type": "string",
                            "description": "A keyword to search for within the article's abstract.",
                        },
                        "full_text_keyword": {
                            "type": "string",
                            "description": "A keyword to search for within the article's full text.",
                        },
                    },
                },
            },
        }
