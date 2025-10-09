from tau_bench.envs.tool import Tool
import json
import uuid
from collections import Counter
from datetime import datetime
from typing import Any

class AddCitation(Tool):
    """Inserts a new citation."""

    @staticmethod
    def invoke(data: dict[str, Any], source_article_id: str = None, cited_article_id: str = None, context: str = None) -> str:
        if not all([source_article_id, cited_article_id]):
            payload = {"error": "source_article_id and cited_article_id are required."}
            out = json.dumps(
                payload)
            return out
        new_citation = {
            "citation_id": f"cit_{uuid.uuid4().hex[:4]}",
            "source_article_id": source_article_id,
            "cited_article_id": cited_article_id,
            "citation_context": context,
        }
        data.get("citations", []).append(new_citation)
        payload = {"success": True, "citation": new_citation}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AddCitation",
                "description": "Adds a new citation.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "source_article_id": {"type": "string"},
                        "cited_article_id": {"type": "string"},
                        "context": {"type": "string"},
                    },
                    "required": ["source_article_id", "cited_article_id"],
                },
            },
        }
