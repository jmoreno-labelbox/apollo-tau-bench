from tau_bench.envs.tool import Tool
import json
from typing import Any

class CalculateTicketMetrics(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], tickets: list[dict[str, Any]]) -> str:
        calculated_tickets = []
        for ticket in tickets:
            ticket["age_hours"] = 72
            ticket["ttr_mins"] = 240
            calculated_tickets.append(ticket)
        payload = calculated_tickets
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "calculateTicketMetrics",
                "description": "Calculates metrics like age and time-to-resolution for a list of tickets.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "tickets": {"type": "array", "items": {"type": "object"}}
                    },
                    "required": ["tickets"],
                },
            },
        }
