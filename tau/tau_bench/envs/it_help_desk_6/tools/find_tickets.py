# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class FindTickets(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any],
        status: Optional[str] = None,
        priority: Optional[str] = None,
        category: Optional[str] = None,
        employee_id: Optional[str] = None,
    ) -> str:
        results = []
        for t in data["tickets"]:
            if status and t["status"] != status:
                continue
            if priority and t["priority"] != priority:
                continue
            if category and t["category"] != category:
                continue
            if employee_id and t["employee_id"] != employee_id:
                continue
            results.append(t)
        return json.dumps({"status": "ok", "tickets": results})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "find_tickets",
                "description": "Find tickets filtered by status, priority, category, and/or employee_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "status": {"type": "string"},
                        "priority": {"type": "string"},
                        "category": {"type": "string"},
                        "employee_id": {"type": "string"},
                    },
                    "required": [],
                },
            },
        }
