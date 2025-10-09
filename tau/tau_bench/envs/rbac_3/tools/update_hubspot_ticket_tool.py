from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any
from datetime import datetime, timedelta

class UpdateHubspotTicketTool(Tool):
    """update_hubspot_ticket
    Modifies ticket fields; deterministically sets updated_at and closed_at when status == CLOSED.
    If actor_id is supplied, also logs an idempotent audit (similar to review_access_request) and
    returns it under 'audit_log' in the response.
    """

    @staticmethod
    def invoke(
        data: dict[str, Any],
        ticket_id: str = None,
        subject: str = None,
        description: str = None,
        status: str = None,
        priority: str = None,
        assignee_id: str = None,
        requester_id: str = None,
        category: str = None,
        actor_id: str = None,
        note: str = None
    ) -> str:
        pass
        if not ticket_id:
            payload = {"error": "ticket_id is required"}
            out = json.dumps(payload, indent=2)
            return out

        updatable_fields = {
            "subject": subject,
            "description": description,
            "status": status,
            "priority": priority,
            "assignee_id": assignee_id,
            "requester_id": requester_id,
            "category": category,
        }

        tickets: list[dict[str, Any]] = data.setdefault("hubspot_tickets", [])
        t = next((x for x in tickets if x.get("ticket_id") == ticket_id), None)
        if not t:
            payload = {"error": f"Ticket {ticket_id} not found"}
            out = json.dumps(payload, indent=2)
            return out

        # Monitor modified fields for audit information
        changed_fields: list[str] = []
        for k, v in updatable_fields.items():
            if v is not None and t.get(k) != v:
                t[k] = v
                changed_fields.append(k)

        if changed_fields:
            t["updated_at"] = _HARD_TS

        if t.get("status") == "CLOSED":
            t["closed_at"] = _HARD_TS

        audit_entry = None
        if actor_id:
            logs = data.setdefault("audit_logs", [])
            log_id = f"LOG-{ticket_id}-update"

            parts = []
            if changed_fields:
                parts.append(f"updated: {', '.join(sorted(changed_fields))}")
            if t.get("status") == "CLOSED":
                parts.append("closed")
            if note:
                parts.append(f"note: {note}")
            details = (
                f"Ticket {ticket_id} " + "; ".join(parts)
                if parts
                else f"Ticket {ticket_id} no changes"
            )

            audit_entry = {
                "log_id": log_id,
                "actor_id": actor_id,
                "action_type": "HUBSPOT_TICKET_UPDATED",
                "target_id": ticket_id,
                "timestamp": _HARD_TS,
                "details": details,
            }
            existing = next((l for l in logs if l.get("log_id") == log_id), None)
            if existing:
                existing.update(audit_entry)
            else:
                logs.append(audit_entry)

        out = dict(t)
        if audit_entry:
            out["audit_log"] = audit_entry
        payload = out
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "updateHubspotTicket",
                "description": (
                    "Update HubSpot ticket fields; sets updated_at deterministically and closed_at when status == CLOSED. "
                    "If actor_id is provided, also records an idempotent audit log and returns it as 'audit_log'."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "ticket_id": {"type": "string"},
                        "subject": {"type": "string"},
                        "description": {"type": "string"},
                        "status": {"type": "string"},
                        "priority": {"type": "string"},
                        "assignee_id": {"type": "string"},
                        "requester_id": {"type": "string"},
                        "category": {"type": "string"},
                        "actor_id": {
                            "type": "string",
                            "description": (
                                "User ID recording the update for audit (e.g., U-005)."
                            ),
                        },
                        "note": {
                            "type": "string",
                            "description": "Optional note to include in the audit log.",
                        },
                    },
                    "required": ["ticket_id"],
                },
            },
        }
