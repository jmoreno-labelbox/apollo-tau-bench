from tau_bench.envs.tool import Tool
import json
from typing import Any

class AttachDocumentToClient(Tool):
    """Link a document to the client's file."""

    @staticmethod
    def invoke(data: dict[str, Any], client_id: str = None, document_id: str = None) -> str:
        if not all([client_id, document_id]):
            payload = {"error": "client_id and document_id are required"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        #Generate an attachment record
        attachment = {
            "attachment_id": 701,
            "client_id": client_id,
            "document_id": document_id,
            "attached_at": "2024-08-21T00:00:00Z",
            "status": "attached",
        }
        payload = {
                "success": True,
                "attachment_id": 701,
                "message": f"Document {document_id} attached to client {client_id}",
                "attachment": attachment,
            }
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "attachDocumentToClient",
                "description": "Attach a document to a client's file",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "client_id": {
                            "type": "integer",
                            "description": "Client ID to attach document to",
                        },
                        "document_id": {
                            "type": "integer",
                            "description": "Document ID to attach",
                        },
                    },
                    "required": ["client_id", "document_id"],
                },
            },
        }
