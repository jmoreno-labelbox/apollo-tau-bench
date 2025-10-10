# Copyright © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class LinkDocumentToClient(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        documents = data.get("documents", [])
        new_id = _next_auto_id(documents, "document_id")
        row = {
            "document_id": new_id,
            "entity_type": "client",
            "entity_id": kwargs.get("client_id"),
            "doc_type": kwargs.get("doc_type") or "briefing_doc",
            "file_uri": kwargs.get("file_uri"),
            "created_by": kwargs.get("created_by"),
            "created_at": _now_iso_fixed(),
        }
        documents.append(row)
        return json.dumps(row, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "link_document_to_client",
                "description": "Attach a provided file_uri to a client as a document.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "client_id": {"type": "integer"},
                        "file_uri": {"type": "string"},
                        "doc_type": {"type": "string"},
                        "created_by": {"type": "integer"},
                    },
                    "required": ["client_id", "file_uri"],
                },
            },
        }
