from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any

class AddPlan(Tool):
    """Creates a new plan."""

    @staticmethod
    def invoke(data: dict[str, Any], plan_id: str = None, date: str = None, author: str = None, allocations: list = None) -> str:
        if not all([plan_id, date, author, allocations]):
            payload = {
                    "error": "plan_id, date, author, and allocations are required parameters."
                }
            out = json.dumps(
                payload)
            return out

        # Fundamental checks for allocations
        if not isinstance(allocations, list):
            payload = {"error": "allocations must be a list."}
            out = json.dumps(payload)
            return out

        total_budget = sum(alloc.get("budget", 0) for alloc in allocations)

        new_plan = {
            "plan_id": plan_id,
            "date": date,
            "total_budget": total_budget,
            "author": author,
            "created_at": "2025-08-13T01:01:01Z",  # Employing a fixed timestamp for uniformity
            "checksum": "manual_override_checksum",
            "allocations": allocations,
        }

        if "plans" not in data:
            data["plans"] = []
        data["plans"].append(new_plan)
        payload = {
                "status": "success",
                "message": f"New plan was added: {new_plan}",
            }
        out = json.dumps(
            payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "addPlan",
                "description": "Adds a new plan.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "plan_id": {"type": "string"},
                        "date": {"type": "string"},
                        "author": {"type": "string"},
                        "allocations": {"type": "array", "items": {"type": "object"}},
                    },
                    "required": ["plan_id", "date", "author", "allocations"],
                },
            },
        }
