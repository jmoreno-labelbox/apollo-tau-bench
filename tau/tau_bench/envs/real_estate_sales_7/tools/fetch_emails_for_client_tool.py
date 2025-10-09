from tau_bench.envs.tool import Tool
import json
import math
import re
from typing import Any

class FetchEmailsForClientTool(Tool):
    """Provides emails for a client with optional filtering and limitations."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        client_id: int,
        template_code: str = None,
        since_date: str = None,
        until_date: str = None,
        limit: int = 50
,
    date: Any = None,
    ) -> str:
        client_id = _as_int(client_id)
        if client_id is None:
            return _err("client_id is required")

        template_filter = template_code
        since_date = since_date  # ISO string, compared in lexicographical order
        until_date = until_date
        limit = _as_int(limit) or 50

        emails = [
            e
            for e in data.get("emails", [])
            if _as_int(e.get("client_id")) == client_id
        ]
        if template_filter:
            emails = [e for e in emails if e.get("template_code") == template_filter]
        if since_date:
            emails = [e for e in emails if (e.get("sent_at") or "") >= since_date]
        if until_date:
            emails = [e for e in emails if (e.get("sent_at") or "") <= until_date]

        emails_sorted = sorted(
            emails, key=lambda e: e.get("sent_at") or "", reverse=True
        )
        out = {
            "client_id": client_id,
            "total": len(emails_sorted),
            "emails": emails_sorted[:limit],
        }
        payload = out
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FetchEmailsForClient",
                "description": (
                    "Fetch emails for a client with optional template and date filters."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "client_id": {"type": "integer"},
                        "template_code": {"type": ["string", "null"]},
                        "since_date": {"type": ["string", "null"]},
                        "until_date": {"type": ["string", "null"]},
                        "limit": {"type": ["integer", "null"]},
                    },
                    "required": ["client_id"],
                },
            },
        }
