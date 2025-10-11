# Copyright Sierra

import datetime
import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool






def _parse_iso(ts: Optional[str]) -> Optional[datetime]:
    """Robust ISO8601 parse: supports 'Z' and offsets; returns None if missing."""
    if not ts:
        return None
    ts = ts.replace("Z", "+00:00")
    return datetime.fromisoformat(ts)

def _eq(a: Optional[str], b: Optional[str]) -> bool:
    return (a or "") == (b or "")

class ListEmailsTool(Tool):
    """list_emails"""

    @staticmethod
    def invoke(data: Dict[str, Any], date_from, date_to, email_id, receiver) -> str:

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