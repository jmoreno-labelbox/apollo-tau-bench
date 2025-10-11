# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateTicket(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any],
        ticket_id: str,
        employee_id: str,
        category: str,
        priority: str,
        status: str,
        subject: str,
        opened_at: str,
        related_asset_id: Optional[str] = None,
    ) -> str:
        row = {
            "ticket_id": ticket_id,
            "employee_id": employee_id,
            "category": category,
            "priority": priority,
            "status": status,
            "subject": subject,
            "opened_at": opened_at,
            "closed_at": None,
            "related_asset_id": related_asset_id,
        }
        _append_row(data["tickets"], row)
        return json.dumps({"status": "ok", "ticket": row})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_ticket",
                "description": "Create a service desk ticket.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "ticket_id": {"type": "string"},
                        "employee_id": {"type": "string"},
                        "category": {"type": "string"},
                        "priority": {"type": "string"},
                        "status": {"type": "string"},
                        "subject": {"type": "string"},
                        "opened_at": {"type": "string"},
                        "related_asset_id": {"type": "string"},
                    },
                    "required": ["ticket_id", "employee_id", "category", "priority", "status", "subject", "opened_at"],
                },
            },
        }
