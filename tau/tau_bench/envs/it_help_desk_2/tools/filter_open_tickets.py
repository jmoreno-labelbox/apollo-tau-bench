# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class FilterOpenTickets(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        tickets = list(data.get("tickets", {}).values())
        open_statuses = ["New", "In Progress", "On Hold", "Open"]
        open_tickets = [t for t in tickets if t.get("status") in open_statuses]
        return json.dumps(open_tickets, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "filter_open_tickets", "description": "Filters a list of tickets to return only those that are not resolved or closed.", "parameters": {"type": "object", "properties": {}, "required": []}}}
