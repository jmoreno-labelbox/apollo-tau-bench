from tau_bench.envs.tool import Tool
import json
from typing import Any

class GetEmailsForClient(Tool):
    """Fetch all emails directed to a particular client."""

    @staticmethod
    def invoke(data: dict[str, Any], client_id: str = None) -> str:
        if not client_id:
            payload = {"error": "client_id is required"}
            out = json.dumps(payload, indent=2)
            return out

        # Retrieve client emails (from database or simulated data)
        emails = data.get("emails", [])
        client_emails = [e for e in emails if e.get("client_id") == client_id]
        payload = {
            "client_id": client_id,
            "email_count": len(client_emails),
            "emails": client_emails,
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
                "name": "getEmailsForClient",
                "description": "Retrieve all emails sent to a specific client",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "client_id": {
                            "type": "integer",
                            "description": "Client ID to get emails for",
                        }
                    },
                    "required": ["client_id"],
                },
            },
        }
