# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CalculateTicketMetrics(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        tickets = kwargs.get("tickets")
        calculated_tickets = []
        for ticket in tickets:
            ticket["age_hours"] = 72
            ticket["ttr_mins"] = 240
            calculated_tickets.append(ticket)
        return json.dumps(calculated_tickets, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "calculate_ticket_metrics", "description": "Calculates metrics like age and time-to-resolution for a list of tickets.", "parameters": {"type": "object", "properties": {"tickets": {"type": "array", "items": {"type": "object"}}}, "required": ["tickets"]}}}
