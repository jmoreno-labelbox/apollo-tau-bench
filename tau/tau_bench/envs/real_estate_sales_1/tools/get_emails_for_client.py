# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetEmailsForClient(Tool):
    """Retrieve all emails sent to a specific client."""
    
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        client_id = kwargs.get('client_id')
        if not client_id:
            return json.dumps({"error": "client_id is required"}, indent=2)
        
        # Get emails for client (from database or mock data)
        emails = data.get('emails', [])
        client_emails = [e for e in emails if e.get('client_id') == client_id]
        
        return json.dumps({
            "client_id": client_id,
            "email_count": len(client_emails),
            "emails": client_emails
        }, indent=2)
    
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_emails_for_client",
                "description": "Retrieve all emails sent to a specific client",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "client_id": {
                            "type": "integer",
                            "description": "Client ID to get emails for"
                        }
                    },
                    "required": ["client_id"]
                }
            }
        }
