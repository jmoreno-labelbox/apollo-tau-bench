# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ComposeClientEmail(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        template_code = kwargs.get("template_code")
        client_id = kwargs.get("client_id")
        subject = (kwargs.get("subject") or template_code)
        slug = (kwargs.get("slug") or f"{template_code}_{client_id}").lower().replace(" ", "_")
        body_uri = f"https://test.storage.com/emails/{slug}.html"
        return json.dumps({"client_id": client_id, "subject": subject, "body_uri": body_uri, "template_code": template_code}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "compose_client_email",
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
