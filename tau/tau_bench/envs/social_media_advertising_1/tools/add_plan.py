# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class AddPlan(Tool):
    """Adds a new plan."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        plan_id = kwargs.get("plan_id")
        date = kwargs.get("date")
        author = kwargs.get("author")
        allocations = kwargs.get("allocations")

        if not all([plan_id, date, author, allocations]):
            return json.dumps({"error": "plan_id, date, author, and allocations are required parameters."})

        # Fundamental checks for allocations
        if not isinstance(allocations, list):
            return json.dumps({"error": "allocations must be a list."})

        total_budget = sum(alloc.get('budget', 0) for alloc in allocations)

        new_plan = {
            "plan_id": plan_id,
            "date": date,
            "total_budget": total_budget,
            "author": author,
            "created_at": "2025-08-13T01:01:01Z",  # Employing a fixed timestamp for uniformity.
            "checksum": "manual_override_checksum",
            "allocations": allocations
        }

        if "plans" not in data:
            data["plans"] = []
        data['plans'].append(new_plan)

        return json.dumps({
            "status": "success",
            "message": f"New plan was added: {new_plan}",
        })

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "add_plan",
                "description": "Adds a new plan.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "plan_id": {"type": "string"},
                        "date": {"type": "string"},
                        "author": {"type": "string"},
                        "allocations": {"type": "array", "items": {"type": "object"}}
                    },
                    "required": ["plan_id", "date", "author", "allocations"],
                },
            },
        }
