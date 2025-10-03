from tau_bench.envs.tool import Tool
import json
from typing import Any

class CreateTicket(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        ticket_id: str,
        employee_id: str,
        category: str,
        priority: str,
        status: str,
        subject: str,
        opened_at: str,
        related_asset_id: str | None = None,
    ) -> str:
        pass
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
        payload = {"status": "ok", "ticket": row}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateTicket",
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
                    "required": [
                        "ticket_id",
                        "employee_id",
                        "category",
                        "priority",
                        "status",
                        "subject",
                        "opened_at",
                    ],
                },
            },
        }
