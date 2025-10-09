from tau_bench.envs.tool import Tool
import json
import uuid
from collections import Counter
from datetime import datetime
from typing import Any

class GetMostCitedArticles(Tool):
    """Utility to obtain a list of the most referenced articles."""

    @staticmethod
    def invoke(data: dict[str, Any], citations: list[dict[str, Any]] = []) -> str:
        cited_ids = [c["referenced_paper_id"] for c in citations]
        citation_counts = Counter(cited_ids)
        sorted_articles = sorted(
            citation_counts.items(), key=lambda item: item[1], reverse=True
        )
        result = [
            {"article_id": article_id, "citation_count": count}
            for article_id, count in sorted_articles
        ]
        payload = result
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetMostCitedArticles",
                "description": "Returns a list of articles sorted by how many times they have been cited.",
                "parameters": {"type": "object", "properties": {}},
            },
        }
