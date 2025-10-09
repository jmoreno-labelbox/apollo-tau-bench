from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class LinkCitedArticle(Tool):
    """Utility for establishing a new citation record linking two articles."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        source_article_id: str = None,
        cited_article_id: str = None,
        citation_context: str = "Citation added for reference."
    ) -> str:
        citations = data.get("citations", [])
        new_citation_id = f"cit_{len(citations) + 1:02d}"
        new_citation = {
            "reference_id": new_citation_id,
            "origin_paper_id": source_article_id,
            "referenced_paper_id": cited_article_id,
            "reference_context": citation_context,
        }
        citations.append(new_citation)
        payload = new_citation
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "LinkCitedArticle",
                "description": "Creates a new citation record to link a source article to a cited article.",
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
                            "description": "A brief description of the citation's context.",
                        },
                    },
                    "required": ["source_article_id", "cited_article_id"],
                },
            },
        }
