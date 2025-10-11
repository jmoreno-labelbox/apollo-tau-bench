# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


def _parse_iso(iso_str: str) -> Optional[str]:
    """Parse ISO 8601 string to datetime."""
    if not iso_str:
        return None
    try:
        from datetime import datetime
        return datetime.fromisoformat(iso_str.replace('Z', '+00:00'))
    except:
        return None


def _eq(a, b) -> bool:
    """Check if two values are equal."""
    return a == b


class ListHubspotTicketsTool(Tool):
    """list_hubspot_tickets"""

    @staticmethod
    def invoke(data: Dict[str, Any], status, category, requester_id, date_from, date_to, ticket_id) -> str:

        dt_from = _parse_iso(date_from)
        dt_to = _parse_iso(date_to)

        tickets: List[Dict[str, Any]] = data.get("hubspot_tickets", [])
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


class GetHubspotTicketsByRequesterTool(Tool):
    """get_hubspot_tickets_by_requester: filter tickets by requester."""

    @staticmethod
    def invoke(data: Dict[str, Any], requester_id) -> str:
        return ListHubspotTicketsTool.invoke(
            data, requester_id=requester_id
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_hubspot_tickets_by_requester",
                "description": "List HubSpot tickets for a requester.",
                "parameters": {
                    "type": "object",
                    "properties": {"requester_id": {"type": "string"}},
                    "required": ["requester_id"],
                },
            },
        }