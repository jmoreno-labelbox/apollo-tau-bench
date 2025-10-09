from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GenerateBriefingDoc(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], client_id: int, broker_id: int, version_tag: str = "v1",
    property_id: Any = None,
    doc_type: Any = None
    ) -> str:
        documents = data.get("documents", {}).values()
        new_id = _next_int_id(documents, "document_id")
        file_uri = f"https://storage.example.com/briefings/client_briefing_{client_id:03d}_{version_tag}.pdf"
        row = {
            "document_id": new_id,
            "entity_type": "client",
            "entity_id": client_id,
            "doc_type": "briefing_doc",
            "file_uri": file_uri,
            "created_by": broker_id,
            "created_at": _fixed_now_iso(),
        }
        data["documents"][row["document_id"]] = row
        payload = {"document_id": new_id, "file_uri": file_uri}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GenerateBriefingDoc",
                "description": "Create a client briefing document and persist it.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "client_id": {"type": "integer"},
                        "broker_id": {"type": "integer"},
                        "version_tag": {"type": "string"},
                    },
                    "required": ["client_id", "broker_id"],
                },
            },
        }
