# Copyright © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class update_company_document_content(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        doc_id = kwargs.get("doc_id")
        new_content = kwargs.get("new_content")

        all_docs = data.get("company_doc", {}).get("company_documents", [])
        doc_to_update = next((d for d in all_docs if d.get("id") == doc_id), None)

        if doc_to_update:
            doc_to_update["content"] = new_content
            doc_to_update["last_updated"] = "2025-06-24"
            return json.dumps(
                {"success": f"Content for document '{doc_id}' updated successfully."},
                indent=2,
            )
        else:
            return json.dumps(
                {"error": f"Company document with ID '{doc_id}' not found."}, indent=2
            )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_company_document_content",
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
