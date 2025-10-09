from tau_bench.envs.tool import Tool
import json
import uuid
from collections import Counter
from datetime import datetime
from typing import Any

class GetAuthorMetrics(Tool):
    """Retrieves various metrics for an author."""

    @staticmethod
    def invoke(data: dict[str, Any], author_name: Any = None) -> str:
        author_name = author_name
        if not author_name:
            payload = {"error": "author_name is required."}
            out = json.dumps(payload)
            return out
        articles = [
            a for a in data.get("articles", []) if author_name in a.get("authors", [])
        ]
        if not articles:
            payload = {"total_publications": 0, "total_citations": 0, "h_index": 0}
            out = json.dumps(
                payload)
            return out
        citations = data.get("citations", [])
        total_citations = 0
        citation_counts = []
        for article in articles:
            count = len(
                [
                    c
                    for c in citations
                    if c.get("referenced_paper_id") == article["paper_id"]
                ]
            )
            total_citations += count
            citation_counts.append(count)
        citation_counts.sort(reverse=True)
        h_index = 0
        for i, count in enumerate(citation_counts):
            if count >= i + 1:
                h_index = i + 1
            else:
                break
        payload = {
                "total_publications": len(articles),
                "total_citations": total_citations,
                "h_index": h_index,
            }
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetAuthorMetrics",
                "description": "Gets multiple metrics for an author.",
                "parameters": {
                    "type": "object",
                    "properties": {"author_name": {"type": "string"}},
                    "required": ["author_name"],
                },
            },
        }
