from tau_bench.envs.tool import Tool
import json
from collections import Counter, defaultdict
from typing import Any

class GetTopCommitAuthors(Tool):
    """Delivers the leading commit authors across all repositories globally."""

    @staticmethod
    def invoke(data: dict[str, Any]) -> str:
        commits = _commits(data)
        counter = Counter()

        for c in commits:
            for author_list in c.get("commit_authors", []):
                counter.update(author_list)

        top_authors = counter.most_common(10)
        payload = [{"author": a, "commits": count} for a, count in top_authors]
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getTopCommitAuthors",
                "description": "Returns top commit authors across all repositories.",
                "parameters": {"type": "object", "properties": {}},
            },
        }
