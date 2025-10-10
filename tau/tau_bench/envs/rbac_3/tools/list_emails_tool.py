# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ListEmailsTool(Tool):
    """list_emails"""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        receiver = kwargs.get("receiver")
        email_id = kwargs.get("email_id")
        date_from = kwargs.get("date_from")
        date_to = kwargs.get("date_to")

        dt_from = _parse_iso(date_from)
        dt_to = _parse_iso(date_to)

        emails: List[Dict[str, Any]] = data.get("emails", [])
        out: List[Dict[str, Any]] = []

        for e in emails:
            if receiver and not _eq(e.get("receiver"), receiver):
                continue
            if email_id and not _eq(e.get("email_id"), email_id):
                continue

            if dt_from or dt_to:
                ts = _parse_iso(e.get("timestamp"))
                if dt_from and (not ts or ts < dt_from):
                    continue
                if dt_to and (not ts or ts > dt_to):
                    continue

            out.append(e)

        out.sort(key=lambda r: ((r.get("timestamp") or ""), (r.get("email_id") or "")))
        return json.dumps(out, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_emails",
                "description": (
                    "List email records with optional filters for receiver, email_id, and date range."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "receiver": {
                            "type": "string",
                            "description": "Email address of the recipient.",
                        },
                        "email_id": {
                            "type": "string",
                            "description": "Specific email record ID (e.g., EM-001)",
                        },
                        "date_from": {
                            "type": "string",
                            "description": "ISO 8601 lower bound for timestamp.",
                        },
                        "date_to": {
                            "type": "string",
                            "description": "ISO 8601 upper bound for timestamp.",
                        },
                    },
                    "required": [],
                },
            },
        }
