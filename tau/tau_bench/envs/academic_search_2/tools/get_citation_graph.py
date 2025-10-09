from tau_bench.envs.tool import Tool
import json
import uuid
from collections import Counter
from datetime import datetime
from typing import Any

class GetCitationGraph(Tool):
    """
    Retrieves the citation graph for a particular article.
    If a second article ID is supplied through 'compare_with_article_id', it identifies the shared citations between both.
    """

    @staticmethod
    def invoke(data: dict[str, Any], article_id: Any = None, compare_with_article_id: Any = None) -> str:
        if not article_id:
            payload = {"error": "article_id is required."}
            out = json.dumps(payload)
            return out

        citations = data.get("citations", [])

        # Functionality taken from the previous FindCommonCitations tool
        if compare_with_article_id:
            cites1 = {
                c["referenced_paper_id"]
                for c in citations
                if c.get("origin_paper_id") == article_id
            }
            cites2 = {
                c["referenced_paper_id"]
                for c in citations
                if c.get("origin_paper_id") == compare_with_article_id
            }
            common_citations = list(cites1.intersection(cites2))
            payload = {
                "article1_id": article_id,
                "article2_id": compare_with_article_id,
                "common_citations": common_citations,
            }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        # Initial logic of GetCitationGraph
        else:
            cited_by = [
                c["origin_paper_id"]
                for c in citations
                if c.get("referenced_paper_id") == article_id
            ]
            cites = [
                c["referenced_paper_id"]
                for c in citations
                if c.get("origin_paper_id") == article_id
            ]
            result = {"article_id": article_id, "cited_by": cited_by, "cites": cites}
            payload = result
            out = json.dumps(payload, indent=2)
            return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetCitationGraph",
                "description": "Gets the citation graph for an article, or finds common citations between two articles.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "article_id": {"type": "string"},
                        "compare_with_article_id": {
                            "type": "string",
                            "description": "If provided, finds common articles cited by both this article and the main article_id.",
                        },
                    },
                    "required": ["article_id"],
                },
            },
        }
