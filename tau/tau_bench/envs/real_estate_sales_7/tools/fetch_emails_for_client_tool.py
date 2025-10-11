# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool






def _err(msg: str, code: str = "bad_request", **extra) -> str:
    out = {"error": msg, "code": code}
    if extra:
        out.update(extra)
    return json.dumps(out, indent=2)

def _as_int(x) -> Optional[int]:
    try:
        return int(x)
    except Exception:
        return None

class FetchEmailsForClientTool(Tool):
    """Returns emails for a client with optional filters and limits."""

    @staticmethod
    def invoke(data: Dict[str, Any], client_id, limit, since_date, template_code, until_date) -> str:
        client_id = _as_int(client_id)
        if client_id is None:
            return _err("client_id is required")

        template_filter = template_code
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
        return json.dumps(out, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "fetch_emails_for_client",
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