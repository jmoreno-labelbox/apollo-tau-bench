# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ListHubspotTicketsTool(Tool):
    """list_hubspot_tickets"""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        status = kwargs.get("status")
        category = kwargs.get("category")
        requester_id = kwargs.get("requester_id")
        date_from = kwargs.get("date_from")
        date_to = kwargs.get("date_to")

        dt_from = _parse_iso(date_from)
        dt_to = _parse_iso(date_to)

        tickets: List[Dict[str, Any]] = data.get("hubspot_tickets", [])
        ticket_id = kwargs.get("ticket_id")
        out: List[Dict[str, Any]] = []
        for t in tickets:
            if ticket_id and not _eq(t.get("ticket_id"), ticket_id):
                continue
            if status and not _eq(t.get("status"), status):
                continue
            if category and not _eq(t.get("category"), category):
                continue
            if requester_id and not _eq(t.get("requester_id"), requester_id):
                continue
            if dt_from or dt_to:
                ts = _parse_iso(t.get("created_at"))
                if dt_from and (not ts or ts < dt_from):
                    continue
                if dt_to and (not ts or ts > dt_to):
                    continue
            out.append(t)

        out.sort(
            key=lambda r: ((r.get("created_at") or ""), (r.get("ticket_id") or ""))
        )
        return json.dumps(out, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_hubspot_tickets",
                "description": "List HubSpot tickets with optional filters.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "ticket_id": {"type": "string"},
                        "status": {"type": "string"},
                        "category": {"type": "string"},
                        "requester_id": {"type": "string"},
                        "date_from": {
                            "type": "string",
                            "description": "ISO 8601 lower bound",
                        },
                        "date_to": {
                            "type": "string",
                            "description": "ISO 8601 upper bound",
                        },
                    },
                    "required": [],
                },
            },
        }
