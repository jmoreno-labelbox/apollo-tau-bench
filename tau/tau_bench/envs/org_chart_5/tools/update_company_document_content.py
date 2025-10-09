from tau_bench.envs.tool import Tool
import json
from collections import Counter
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class update_company_document_content(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], doc_id: str = None, new_content: str = None) -> str:
        all_docs = data.get("company_doc", {}).values().get("company_documents", [])
        doc_to_update = next((d for d in all_docs.values() if d.get("id") == doc_id), None)

        if doc_to_update:
            doc_to_update["content"] = new_content
            doc_to_update["last_updated"] = "2025-06-24"
            payload = {"success": f"Content for document '{doc_id}' updated successfully."}
            out = json.dumps(
                payload, indent=2,
            )
            return out
        else:
            payload = {"error": f"Company document with ID '{doc_id}' not found."}
            out = json.dumps(
                payload, indent=2
            )
            return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateCompanyDocumentContent",
                "description": "Updates the full text content of an existing company-wide document.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "doc_id": {"type": "string"},
                        "new_content": {"type": "string"},
                    },
                    "required": ["doc_id", "new_content"],
                },
            },
        }
