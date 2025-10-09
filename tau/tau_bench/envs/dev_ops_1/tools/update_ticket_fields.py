from tau_bench.envs.tool import Tool
import json
from typing import Any

class UpdateTicketFields(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], ticket_key: str, fields: dict[str, Any]) -> str:
        work_items = _get_table(data, "work_items")
        item = next(
            (
                w
                for w in work_items
                if w.get("ticket_key") == ticket_key or w.get("id") == ticket_key
            ),
            None,
        )
        if not item:
            return _error(f"Ticket '{ticket_key}' not found.")
        item.update(fields or {})
        payload = {"updated": True}
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateTicketFields",
                "description": "Updates fields on a ticket deterministically.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "ticket_key": {"type": "string"},
                        "fields": {"type": "object"},
                    },
                    "required": ["ticket_key", "fields"],
                },
            },
        }
