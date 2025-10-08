from tau_bench.envs.tool import Tool
import json
from typing import Any

class FindTickets(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        status: str | None = None,
        priority: str | None = None,
        category: str | None = None,
        employee_id: str | None = None,
    ) -> str:
        pass
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
        payload = {"status": "ok", "tickets": results}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "FindTickets",
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
