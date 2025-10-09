from tau_bench.envs.tool import Tool
import json
from itertools import islice
from typing import Any

class ComposeClientEmail(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], template_code: str = None, client_id: str = None, subject: str = None, slug: str = None) -> str:
        subject = subject or template_code
        slug = (slug or f"{template_code}_{client_id}").lower().replace(" ", "_")
        body_uri = f"https://test.storage.com/emails/{slug}.html"
        payload = {
            "client_id": client_id,
            "subject": subject,
            "body_uri": body_uri,
            "template_code": template_code,
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
                "name": "ComposeClientEmail",
                "description": "Render email body and return body_uri for a template + client.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "template_code": {"type": "string"},
                        "client_id": {"type": "integer"},
                        "subject": {"type": "string"},
                        "slug": {"type": "string"},
                        "payload": {"type": "object"},
                    },
                    "required": ["template_code", "client_id"],
                },
            },
        }
