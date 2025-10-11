# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetTopCommitAuthors(Tool):
    """Returns top commit authors globally across all repositories."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        commits = _commits(data)
        counter = Counter()

        for c in commits:
            for author_list in c.get("commit_authors", []):
                counter.update(author_list)

        top_authors = counter.most_common(10)
        return json.dumps([{"author": a, "commits": count} for a, count in top_authors], indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_top_commit_authors",
                "description": "Returns top commit authors across all repositories.",
                "parameters": {
                    "type": "object",
                    "properties": {}
                }
            }
        }
