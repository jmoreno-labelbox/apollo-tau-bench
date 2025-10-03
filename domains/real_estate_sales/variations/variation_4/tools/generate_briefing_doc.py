from tau_bench.envs.tool import Tool
import json
from typing import Any

class GenerateBriefingDoc(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], client_id: str = None, broker_id: str = None,
        property_id: Any = None,
        doc_type: Any = None,
    ) -> str:
        if not all([client_id, broker_id]):
            payload = {"error": "client_id and broker_id are required"}
            out = json.dumps(
                payload, indent=2
            )
            return out

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
            "created_at": "2024-08-21T00:00:00Z",
        }
        payload = {
                "success": True,
                "document_id": document_id,
                "message": f"Briefing document generated for client {client_id}",
                "document": document,
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
                "name": "GenerateBriefingDoc",
                "description": "Generate a briefing document for a client",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "client_id": {
                            "type": "integer",
                            "description": "Client ID to generate briefing for",
                        },
                        "broker_id": {
                            "type": "integer",
                            "description": "Broker ID generating the briefing",
                        },
                    },
                    "required": ["client_id", "broker_id"],
                },
            },
        }
