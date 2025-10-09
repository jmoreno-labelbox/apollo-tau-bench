from tau_bench.envs.tool import Tool
import json
from itertools import islice
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class LinkDocumentToClient(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], client_id: str, doc_type: str = "briefing_doc", file_uri: str = None, created_by: str = None,
    document_id: Any = None,
    ) -> str:
        documents = data.get("documents", {}).values()
        new_id = _next_auto_id(documents, "document_id")
        row = {
            "document_id": new_id,
            "entity_type": "client",
            "entity_id": client_id,
            "doc_type": doc_type,
            "file_uri": file_uri,
            "created_by": created_by,
            "created_at": _now_iso_fixed(),
        }
        data["documents"][document_id] = row
        payload = row
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "LinkDocumentToClient",
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
