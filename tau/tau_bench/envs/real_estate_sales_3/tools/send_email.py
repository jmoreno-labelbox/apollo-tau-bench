from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class SendEmail(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        client_id: str = None,
        broker_id: str = None,
        subject: str = None,
        body_uri: str = None,
        template_code: str = None,
        campaign_id: str = None
    ) -> str:
        emails = data.get("emails", [])
        new_email_id = _next_int_id(emails, "email_id")
        row = {
            "email_id": new_email_id,
            "client_id": client_id,
            "broker_id": broker_id,
            "subject": subject,
            "body_uri": body_uri,
            "template_code": template_code,
            "sent_at": _fixed_now_iso(),
            "campaign_id": campaign_id,
        }
        emails.append(row)
        payload = row
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SendEmail",
                "description": "Persist an outbound email.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "client_id": {"type": "integer"},
                        "broker_id": {"type": "integer"},
                        "subject": {"type": "string"},
                        "body_uri": {"type": "string"},
                        "template_code": {"type": "string"},
                        "campaign_id": {"type": ["integer", "null"]},
                    },
                    "required": [
                        "client_id",
                        "broker_id",
                        "subject",
                        "body_uri",
                        "template_code",
                    ],
                },
            },
        }
