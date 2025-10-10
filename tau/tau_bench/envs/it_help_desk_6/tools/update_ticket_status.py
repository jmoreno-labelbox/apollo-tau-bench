# Copyright © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateTicketStatus(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], ticket_id: str, status: str, closed_at: Optional[str] = None) -> str:
        t = _find_one(data["tickets"], ticket_id=ticket_id)
        if not t:
            return json.dumps({"status": "error", "reason": "ticket_not_found"})
        valid = {"New", "Open", "In Progress", "On Hold", "Resolved", "Closed"}
        if status not in valid:
            return json.dumps({"status": "error", "reason": "invalid_status"})
        t["status"] = status
        if closed_at is not None:
            t["closed_at"] = closed_at
        return json.dumps({"status": "ok", "ticket": t})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_ticket_status",
                "description": "Update a ticket's status and optional closed_at timestamp.",
                "parameters": {
                    "type": "object",
                    "properties": {"ticket_id": {"type": "string"}, "status": {"type": "string"}, "closed_at": {"type": "string"}},
                    "required": ["ticket_id", "status"],
                },
            },
        }
