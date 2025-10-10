# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class SendEmail(Tool):
    """Send an email to a client and record it in the system."""
    
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        client_id = kwargs.get('client_id')
        broker_id = kwargs.get('broker_id')
        subject = kwargs.get('subject')
        template_code = kwargs.get('template_code')
        body_uri = kwargs.get('body_uri')
        campaign_id = kwargs.get('campaign_id')
        
        if not all([client_id, broker_id, subject, template_code]):
            return json.dumps({
                "error": "client_id, broker_id, subject, and template_code are required"
            }, indent=2)
        
        # Create email record with unique ID
        import time
        timestamp = str(int(time.time() * 1000))  # millisecond timestamp
        email_id = f"EMAIL-{client_id}-{timestamp}"
        email = {
            "email_id": email_id,
            "client_id": client_id,
            "broker_id": broker_id,
            "subject": subject,
            "template_code": template_code,
            "body_uri": body_uri,
            "campaign_id": campaign_id,
            "sent_at": "2024-08-21T00:00:00Z",
            "status": "sent"
        }
        
        return json.dumps({
            "success": True,
            "email_id": email_id,
            "message": f"Email sent to client {client_id}",
            "email": email
        }, indent=2)
    
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "send_email",
                "description": "Send an email to a client and record it",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "client_id": {
                            "type": "integer",
                            "description": "Client ID to send email to"
                        },
                        "broker_id": {
                            "type": "integer",
                            "description": "Broker ID sending the email"
                        },
                        "subject": {
                            "type": "string",
                            "description": "Email subject line"
                        },
                        "template_code": {
                            "type": "string",
                            "description": "Email template code"
                        },
                        "body_uri": {
                            "type": "string",
                            "description": "URI to email body content"
                        },
                        "campaign_id": {
                            "type": "integer",
                            "description": "Campaign ID to associate with email"
                        }
                    },
                    "required": ["client_id", "broker_id", "subject", "template_code"]
                }
            }
        }
