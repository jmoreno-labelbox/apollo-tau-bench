from tau_bench.envs.tool import Tool
import json
from typing import Any

class SendEmail(Tool):
    """Dispatch an email to a client and log it in the system."""

    @staticmethod
    def invoke(
        data: dict[str, Any], 
        client_id: str = None, 
        broker_id: str = None, 
        subject: str = None, 
        template_code: str = None, 
        body_uri: str = None, 
        campaign_id: str = None, type: Any = None) -> str:
        pass

        if not all([client_id, broker_id, subject, template_code]):
            payload = {
                    "error": "client_id, broker_id, subject, and template_code are required"
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        #Generate an email record with a distinct identifier
        import time

        timestamp = str(int(time.time() * 1000))  #timestamp in milliseconds
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
            "status": "sent",
        }
        payload = {
                "success": True,
                "email_id": email_id,
                "message": f"Email sent to client {client_id}",
                "email": email,
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
                "name": "SendEmail",
                "description": "Send an email to a client and record it",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "client_id": {
                            "type": "integer",
                            "description": "Client ID to send email to",
                        },
                        "broker_id": {
                            "type": "integer",
                            "description": "Broker ID sending the email",
                        },
                        "subject": {
                            "type": "string",
                            "description": "Email subject line",
                        },
                        "template_code": {
                            "type": "string",
                            "description": "Email template code",
                        },
                        "body_uri": {
                            "type": "string",
                            "description": "URI to email body content",
                        },
                        "campaign_id": {
                            "type": "integer",
                            "description": "Campaign ID to associate with email",
                        },
                    },
                    "required": ["client_id", "broker_id", "subject", "template_code"],
                },
            },
        }
