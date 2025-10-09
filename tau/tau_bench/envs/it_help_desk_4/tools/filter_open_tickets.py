from tau_bench.envs.tool import Tool
import json
from typing import Any

class FilterOpenTickets(Tool):
    @staticmethod
    def invoke(data: dict[str, Any]) -> str:
        tickets = data.get("tickets", [])
        open_statuses = ["New", "In Progress", "On Hold", "Open"]
        open_tickets = [t for t in tickets if t.get("status") in open_statuses]
        payload = open_tickets
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "filterOpenTickets",
                "description": "Filters a list of tickets to return only those that are not resolved or closed.",
                "parameters": {"type": "object", "properties": {}, "required": []},
            },
        }
