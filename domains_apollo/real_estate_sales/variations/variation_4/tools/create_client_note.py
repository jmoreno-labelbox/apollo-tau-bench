from tau_bench.envs.tool import Tool
import json
from typing import Any

class CreateClientNote(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], client_id: str = None, broker_id: str = None, note_text: str = None, note_type: str = "general", neighborhood_name: Any = None) -> str:
        if not all([client_id, broker_id, note_text]):
            payload = {"error": "client_id, broker_id, and note_text are required"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        note = {
            "note_id": 801,
            "client_id": client_id,
            "broker_id": broker_id,
            "note_text": note_text,
            "note_type": note_type,
            "created_at": "2024-08-21T00:00:00Z",
            "status": "active",
        }
        payload = {
                "success": True,
                "note_id": 801,
                "message": f"Note created for client {client_id}",
                "note": note,
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
                "name": "createClientNote",
                "description": "Create a note for a client's file",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "client_id": {
                            "type": "integer",
                            "description": "Client ID to create note for",
                        },
                        "broker_id": {
                            "type": "integer",
                            "description": "Broker ID creating the note",
                        },
                        "note_text": {
                            "type": "string",
                            "description": "Content of the note",
                        },
                        "note_type": {
                            "type": "string",
                            "description": "Type of note (general, follow_up, concern, etc.)",
                        },
                    },
                    "required": ["client_id", "broker_id", "note_text"],
                },
            },
        }
