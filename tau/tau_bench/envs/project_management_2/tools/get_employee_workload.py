from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class GetEmployeeWorkload(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], employee_id: str = None, sprint_id: str = None, include_blocked: bool = True) -> str:
        if not employee_id:
            payload = {"error": "employee_id is required"}
            out = json.dumps(payload)
            return out

        tasks = data.get("tasks", {}).values()

        employee_tasks = [t for t in tasks.values() if t.get("assignee_id") == employee_id]

        if sprint_id:
            employee_tasks = [
                t for t in employee_tasks if t.get("sprint_id") == sprint_id
            ]

        active_tasks = [
            t for t in employee_tasks if t.get("status") in ["in_progress", "todo"]
        ]
        if include_blocked:
            active_tasks.extend(
                [t for t in employee_tasks.values() if t.get("status") == "blocked"]
            )

        total_story_points = sum(t.get("story_points", 0) for t in active_tasks.values())

        status_breakdown = {
            "todo": len([t for t in employee_tasks.values() if t.get("status") == "todo"]),
            "in_progress": len(
                [t for t in employee_tasks.values() if t.get("status") == "in_progress"]
            ),
            "blocked": len([t for t in employee_tasks.values() if t.get("status") == "blocked"]),
            "done": len([t for t in employee_tasks.values() if t.get("status") == "done"]),
        }

        priority_breakdown = {
            "critical": sum(
                t.get("story_points", 0)
                for t in active_tasks
                if t.get("priority") == "critical"
            ),
            "high": sum(
                t.get("story_points", 0)
                for t in active_tasks
                if t.get("priority") == "high"
            ),
            "medium": sum(
                t.get("story_points", 0)
                for t in active_tasks
                if t.get("priority") == "medium"
            ),
            "low": sum(
                t.get("story_points", 0)
                for t in active_tasks
                if t.get("priority") == "low"
            ),
        }
        payload = {
                "employee_id": employee_id,
                "sprint_id": sprint_id,
                "total_active_story_points": total_story_points,
                "total_tasks": len(employee_tasks),
                "active_tasks": len(active_tasks),
                "status_breakdown": status_breakdown,
                "priority_breakdown": priority_breakdown,
                "workload_rating": (
                    "overloaded"
                    if total_story_points > 25
                    else "high" if total_story_points > 20 else "normal"
                ),
            }
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetEmployeeWorkload",
                "description": "Get current workload for an employee",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "employee_id": {
                            "type": "string",
                            "description": "The employee ID",
                        },
                        "sprint_id": {
                            "type": "string",
                            "description": "Optional sprint ID to filter by",
                        },
                        "include_blocked": {
                            "type": "boolean",
                            "description": "Include blocked tasks in workload calculation",
                        },
                    },
                    "required": ["employee_id"],
                },
            },
        }
