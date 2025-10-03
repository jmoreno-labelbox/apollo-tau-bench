from tau_bench.envs.tool import Tool
import json
from itertools import islice
from typing import Any

class PersistOutboundEmail(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], client_id: str = None, broker_id: str = None, subject: str = None, body_uri: str = None, template_code: str = None, campaign_id: str = None) -> str:
        emails = data.get("emails", [])
        new_email_id = _next_auto_id(emails, "email_id")
        row = {
            "email_id": new_email_id,
            "client_id": client_id,
            "broker_id": broker_id,
            "subject": subject,
            "body_uri": body_uri,
            "template_code": template_code,
            "sent_at": _now_iso_fixed(),
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
                "name": "PersistOutboundEmail",
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
