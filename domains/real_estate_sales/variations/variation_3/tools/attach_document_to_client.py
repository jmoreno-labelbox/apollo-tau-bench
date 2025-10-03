from tau_bench.envs.tool import Tool
import json
from typing import Any

class AttachDocumentToClient(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], client_id: str, doc_type: str = "briefing_doc", file_uri: str = None, created_by: str = None, property_id: Any = None,
    document_id: Any = None,
    ) -> str:
        documents = data.get("documents", [])
        new_id = _next_int_id(documents, "document_id")
        row = {
            "document_id": new_id,
            "entity_type": "client",
            "entity_id": client_id,
            "doc_type": doc_type,
            "file_uri": file_uri,
            "created_by": created_by,
            "created_at": _fixed_now_iso(),
        }
        documents.append(row)
        payload = row
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AttachDocumentToClient",
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
