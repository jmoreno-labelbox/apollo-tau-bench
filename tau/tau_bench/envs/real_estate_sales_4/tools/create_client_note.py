# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateClientNote(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], broker_id, client_id, note_text, note_type = 'general') -> str:
        
        if not all([client_id, broker_id, note_text]):
            return json.dumps({
                "error": "client_id, broker_id, and note_text are required"
            }, indent=2)
        
        note = {
            "note_id": 801,
            "client_id": client_id,
            "broker_id": broker_id,
            "note_text": note_text,
            "note_type": note_type,
            "created_at": "2024-08-21T00:00:00Z",
            "status": "active"
        }
        
        return json.dumps({
            "success": True,
            "note_id": 801,
            "message": f"Note created for client {client_id}",
            "note": note
        }, indent=2)
    
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_client_note",
                "description": "Create a note for a client's file",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "client_id": {
                            "type": "integer",
                            "description": "Client ID to create note for"
                        },
                        "broker_id": {
                            "type": "integer",
                            "description": "Broker ID creating the note"
                        },
                        "note_text": {
                            "type": "string",
                            "description": "Content of the note"
                        },
                        "note_type": {
                            "type": "string",
                            "description": "Type of note (general, follow_up, concern, etc.)"
                        }
                    },
                    "required": ["client_id", "broker_id", "note_text"]
                }
            }
        }
