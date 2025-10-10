# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GenerateBriefingDoc(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], broker_id, client_id) -> str:
        
        if not all([client_id, broker_id]):
            return json.dumps({
                "error": "client_id and broker_id are required"
            }, indent=2)
        
        import time
        timestamp = str(int(time.time() * 1000))
        document_id = f"DOC-{client_id}-{timestamp}"
        document = {
            "document_id": document_id,
            "client_id": client_id,
            "broker_id": broker_id,
            "document_type": "briefing",
            "title": f"Client Briefing - Client {client_id}",
            "file_path": f"https://storage.example.com/briefings/client_{client_id}_briefing.pdf",
            "status": "generated",
            "created_at": "2024-08-21T00:00:00Z"
        }
        
        return json.dumps({
            "success": True,
            "document_id": document_id,
            "message": f"Briefing document generated for client {client_id}",
            "document": document
        }, indent=2)
    
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "generate_briefing_doc",
                "description": "Generate a briefing document for a client",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "client_id": {
                            "type": "integer",
                            "description": "Client ID to generate briefing for"
                        },
                        "broker_id": {
                            "type": "integer",
                            "description": "Broker ID generating the briefing"
                        }
                    },
                    "required": ["client_id", "broker_id"]
                }
            }
        }
