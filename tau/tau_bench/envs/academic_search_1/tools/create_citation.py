from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime
from typing import Any

class CreateCitation(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], source_article_id: Any = None, cited_article_id: Any = None, citation_context: Any = None) -> str:
        source_article_id = source_article_id
        cited_article_id = cited_article_id
        context = citation_context
        if not all([source_article_id, cited_article_id]):
            payload = {"error": "source_article_id and cited_article_id are required."}
            out = json.dumps(payload)
            return out

        new_id = f"cit_{uuid.uuid4().hex[:4]}"
        new_citation = {
            "reference_id": new_id,
            "origin_paper_id": source_article_id,
            "referenced_paper_id": cited_article_id,
            "reference_context": context,
        }
        data["citations"].append(new_citation)
        payload = {"success": True, "citation": new_citation}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateCitation",
                "description": "Creates a new citation, linking a source article to a cited article.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "source_article_id": {
                            "type": "string",
                            "description": "The ID of the article making the citation.",
                        },
                        "cited_article_id": {
                            "type": "string",
                            "description": "The ID of the article being cited.",
                        },
                        "citation_context": {
                            "type": "string",
                            "description": "The sentence or context in which the citation is made.",
                        },
                    },
                    "required": ["source_article_id", "cited_article_id"],
                },
            },
        }
