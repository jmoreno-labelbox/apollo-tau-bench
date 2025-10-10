# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class FindCollaborationNetwork(Tool):
    """
    Finds the collaboration network for a given author.
    Can be constrained to check only against a specific list of potential collaborators.
    """
    @staticmethod
    def invoke(data: Dict[str, Any], author_name, authors_to_check) -> str:
        if not author_name:
            return json.dumps({"error": "author_name is required."})

        # Retrieve all publications by the primary author.
        articles = [a for a in list(data.get('articles', {}).values()) if author_name in a.get('authors', [])]

        # Calculate the total number of contributors from the specified articles.
        all_collaborators = Counter()
        for article in articles:
            for author in article.get('authors', []):
                if author != author_name:
                    all_collaborators[author] += 1

        # Filter the results based on the given list of authors.
        if authors_to_check:
            final_counts = {author: all_collaborators.get(author, 0) for author in authors_to_check}
            return json.dumps(final_counts, indent=2)

        return json.dumps(dict(all_collaborators), indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "find_collaboration_network", "description": "Finds the collaboration network for an author, optionally checking against a specific list of names.", "parameters": {"type": "object", "properties": {"author_name": {"type": "string"}, "authors_to_check": {"type": "array", "items": {"type": "string"}}}, "required": ["author_name"]}}}
