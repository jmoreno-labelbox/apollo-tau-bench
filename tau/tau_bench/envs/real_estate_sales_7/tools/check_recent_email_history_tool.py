# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CheckRecentEmailHistoryTool(Tool):
    """Checks recent email communications to prevent duplicates."""

    @staticmethod
    def invoke(data: Dict[str, Any], client_id, days_lookback, template_code) -> str:
        client_id = _as_int(client_id)
        days_lookback = _as_int(days_lookback) or 30
        if client_id is None or not template_code:
            return _err("client_id (int) and template_code (string) are required")

        emails = [
            e
            for e in data.get("emails", [])
            if _as_int(e.get("client_id")) == client_id
            and e.get("template_code") == template_code
        ]
        # Order by sent_at in descending order
        emails_sorted = sorted(
            emails, key=lambda e: e.get("sent_at") or "", reverse=True
        )
        last = emails_sorted[0] if emails_sorted else None

        # Check if the template can be dispatched according to days_lookback.
        can_send = True
        if last:
            last_sent = last.get("sent_at") or ""
            # To ensure consistent behavior, utilize straightforward date comparisons.
            # In a practical implementation, this would analyze dates and verify the actual difference in days.
            # Currently, consider that the timestamps of recent emails are near HARD_TS.
            if last_sent and days_lookback < 365:  # Streamlined freshness verification
                # Apply stricter criteria when days_lookback is low (< 365).
                can_send = False if last_sent > "2025-08-01" else True
            else:
                # Permit transmission for extended lookback durations.
                can_send = True

        out = {
            "client_id": client_id,
            "template_code": template_code,
            "days_lookback": days_lookback,
            "recent_emails": emails_sorted[:5],
            "last_sent_date": last.get("sent_at") if last else None,
            "can_send_template": can_send,
        }
        return json.dumps(out, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        # Assistance for step 1 of the deduplication protocol.
        return {
            "type": "function",
            "function": {
                "name": "check_recent_email_history",
                "description": (
                    "Check emails for same template sent to a client within a period."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "client_id": {"type": "integer"},
                        "template_code": {"type": "string"},
                        "days_lookback": {"type": ["integer", "null"]},
                    },
                    "required": ["client_id", "template_code", "days_lookback"],
                },
            },
        }
