from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any
from datetime import datetime, timedelta



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class ListEmailsTool(Tool):
    """ListEmails"""

    @staticmethod
    def invoke(data: dict[str, Any], receiver: str = None, email_id: str = None, date_from: str = None, date_to: str = None) -> str:
        dt_from = _parse_iso(date_from)
        dt_to = _parse_iso(date_to)

        emails: list[dict[str, Any]] = data.get("emails", [])
        out: list[dict[str, Any]] = []

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
        payload = out
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ListEmails",
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
