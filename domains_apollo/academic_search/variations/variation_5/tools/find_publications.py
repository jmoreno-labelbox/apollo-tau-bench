from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime
from typing import Any

class FindPublications(Tool):
    """Utility for locating articles according to different criteria."""

    @staticmethod
    def invoke(data: dict[str, Any], *, title: Any = None, author_name: Any = None, topic: Any = None, publication_year: Any = None, article_id: Any = None) -> str:
        if not any([title, author_name, topic, publication_year, article_id]):
            payload = {"error": "At least one search parameter is required."}
            out = json.dumps(payload)
            return out

        articles = data.get("articles", [])
        results = []
        for article in articles:
            title_match = not title or title.lower() in article.get("title", "").lower()
            author_match = not author_name or any(
                author_name.lower() in author.lower()
                for author in article.get("authors", [])
            )
            topic_match = not topic or topic.lower() == article.get("topic", "").lower()
            year_match = not publication_year or str(publication_year) == str(
                article.get("publication_year")
            )
            id_match = not article_id or article_id == article.get("article_id")

            if all([title_match, author_match, topic_match, year_match, id_match]):
                results.append(article)
        payload = results
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FindPublications",
                "description": "Searches for articles by title, author, topic, or publication year.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "title": {
                            "type": "string",
                            "description": "The title or a keyword from the title of the article.",
                        },
                        "author_name": {
                            "type": "string",
                            "description": "The name of one of the authors.",
                        },
                        "topic": {
                            "type": "string",
                            "description": "The main topic of the article (e.g., 'AI', 'Biomedicine').",
                        },
                        "publication_year": {
                            "type": "integer",
                            "description": "The year the article was published.",
                        },
                        "article_id": {
                            "type": "string",
                            "description": "The exact ID of the article.",
                        },
                    },
                },
            },
        }
