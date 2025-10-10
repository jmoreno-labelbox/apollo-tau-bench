# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GenerateClientBriefingDocumentTool(Tool):
    """Generates a client briefing PDF and inserts a documents row (entity_type=client)."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        client_id = _as_int(kwargs.get("client_id"))
        created_by = _as_int(kwargs.get("created_by"))
        if client_id is None or created_by is None:
            return _err("client_id and created_by are required")

        docs = data.setdefault("documents", [])
        document_id = _next_int_id(docs, "document_id")
        padded = str(client_id).zfill(3)
        uri = f"https://storage.example.com/briefings/client_briefing_{padded}.pdf"

        doc_row = {
            "document_id": document_id,
            "entity_type": "client",
            "entity_id": int(client_id),
            "doc_type": "briefing_doc",
            "file_uri": uri,
            "created_by": int(created_by),
            "created_at": HARD_TS,
        }
        docs.append(doc_row)

        return json.dumps({"document": doc_row}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "generate_client_briefing_document",
                "description": (
                    "Generate client briefing PDF and insert into documents table."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "client_id": {"type": "integer"},
                        "created_by": {"type": "integer"},
                    },
                    "required": ["client_id", "created_by"],
                },
            },
        }
