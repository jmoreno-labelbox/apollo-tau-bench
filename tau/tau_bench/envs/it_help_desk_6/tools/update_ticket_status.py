from tau_bench.envs.tool import Tool
import json
from typing import Any

class UpdateTicketStatus(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any], ticket_id: str, status: str, closed_at: str | None = None
    ) -> str:
        pass
        t = _find_one(data["tickets"], ticket_id=ticket_id)
        if not t:
            payload = {"status": "error", "reason": "ticket_not_found"}
            out = json.dumps(payload)
            return out
        valid = {"New", "Open", "In Progress", "On Hold", "Resolved", "Closed"}
        if status not in valid:
            payload = {"status": "error", "reason": "invalid_status"}
            out = json.dumps(payload)
            return out
        t["status"] = status
        if closed_at is not None:
            t["closed_at"] = closed_at
        payload = {"status": "ok", "ticket": t}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateTicketStatus",
                "description": "Update a ticket's status and optional closed_at timestamp.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "ticket_id": {"type": "string"},
                        "status": {"type": "string"},
                        "closed_at": {"type": "string"},
                    },
                    "required": ["ticket_id", "status"],
                },
            },
        }
