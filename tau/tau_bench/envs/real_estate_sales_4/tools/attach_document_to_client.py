# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class AttachDocumentToClient(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        client_id = kwargs.get('client_id')
        document_id = kwargs.get('document_id')
        
        if not all([client_id, document_id]):
            return json.dumps({
                "error": "client_id and document_id are required"
            }, indent=2)
        
        attachment = {
            "attachment_id": 701,
            "client_id": client_id,
            "document_id": document_id,
            "attached_at": "2024-08-21T00:00:00Z",
            "status": "attached"
        }
        
        return json.dumps({
            "success": True,
            "attachment_id": 701,
            "message": f"Document {document_id} attached to client {client_id}",
            "attachment": attachment
        }, indent=2)
    
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "attach_document_to_client",
                "description": "Attach a document to a client's file",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "client_id": {
                            "type": "integer",
                            "description": "Client ID to attach document to"
                        },
                        "document_id": {
                            "type": "integer",
                            "description": "Document ID to attach"
                        }
                    },
                    "required": ["client_id", "document_id"]
                }
            }
        }
