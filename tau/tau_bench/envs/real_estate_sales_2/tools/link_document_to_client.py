# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool






def _now_iso_fixed() -> str:
    return "2025-08-20T00:00:00Z"

def _next_auto_id(rows: List[Dict[str, Any]], key: str) -> int:
    return max((int(r.get(key, 0)) for r in rows), default=0) + 1

class LinkDocumentToClient(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], client_id, created_by, doc_type, file_uri) -> str:
        documents = data.get("documents", [])
        new_id = _next_auto_id(documents, "document_id")
        row = {
            "document_id": new_id,
            "entity_type": "client",
            "entity_id": client_id,
            "doc_type": doc_type or "briefing_doc",
            "file_uri": file_uri,
            "created_by": created_by,
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