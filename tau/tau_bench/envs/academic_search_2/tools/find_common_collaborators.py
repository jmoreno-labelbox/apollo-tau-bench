# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class FindCommonCollaborators(Tool):
    """Finds common collaborators between two authors."""
    @staticmethod
    def invoke(data: Dict[str, Any], author1_name, author2_name) -> str:
        author1_name, author2_name = author1_name, author2_name
        if not all([author1_name, author2_name]):
            return json.dumps({"error": "author1_name and author2_name are required."})
        articles1 = [a for a in list(data.get('articles', {}).values()) if author1_name in a.get('authors', [])]
        collaborators1 = {author for article in articles1 for author in article.get('authors', []) if author != author1_name}
        articles2 = [a for a in list(data.get('articles', {}).values()) if author2_name in a.get('authors', [])]
        collaborators2 = {author for article in articles2 for author in article.get('authors', []) if author != author2_name}
        common_collaborators = list(collaborators1.intersection(collaborators2))
        return json.dumps({"common_collaborators": common_collaborators}, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "find_common_collaborators", "description": "Finds common collaborators between two authors.", "parameters": {"type": "object", "properties": {"author1_name": {"type": "string"}, "author2_name": {"type": "string"}}, "required": ["author1_name", "author2_name"]}}}
