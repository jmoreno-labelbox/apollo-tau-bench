# Sierra Copyright

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class RegisterArticleRecord(Tool):
    """Tool to create a new article record."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        articles = list(data.get('articles', {}).values())
        new_article = {
            "article_id": f"art_{len(articles) + 1:02d}",
            "title": kwargs.get('title'),
            "authors": kwargs.get('authors', []),
            "publication_year": datetime.now().year,
            "topic": kwargs.get('topic'),
            "abstract": kwargs.get('abstract'),
            "status": "draft"
        }
        articles.append(new_article)
        return json.dumps(new_article, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "register_article_record", "description": "Creates a new draft article record.", "parameters": {"type": "object", "properties": {
            "title": {"type": "string", "description": "The title of the article."},
            "authors": {"type": "array", "items": {"type": "string"}, "description": "A list of author names."},
            "topic": {"type": "string", "description": "The primary topic of the article."},
            "abstract": {"type": "string", "description": "The abstract of the article."}
        }, "required": ["title", "authors", "topic", "abstract"]}}}
