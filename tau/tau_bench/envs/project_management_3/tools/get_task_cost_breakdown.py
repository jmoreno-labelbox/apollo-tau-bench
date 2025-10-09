from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime, timezone
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetTaskCostBreakdown(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], task_id: str = None) -> str:
        if not task_id:
            payload = {"error": "task_id is required"}
            out = json.dumps(payload)
            return out

        tasks = data.get("tasks", [])
        task_logs = data.get("task_logs", [])
        employees = data.get("employees", [])
        expenses = data.get("expenses", [])

        task = next((t for t in tasks if t.get("task_id") == task_id), None)
        if not task:
            payload = {"error": f"Task {task_id} not found"}
            out = json.dumps(payload)
            return out

        task_time_logs = [log for log in task_logs if log.get("task_id") == task_id]

        personnel_costs = []
        total_hours = 0
        total_personnel_cost = 0

        for log in task_time_logs:
            employee_id = log.get("employee_id")
            hours = log.get("hours", 0)

            employee = next(
                (e for e in employees if e.get("employee_id") == employee_id), None
            )
            if employee:
                hourly_rate = (
                    150 if "senior" in employee.get("role", "").lower() else 100
                )
                cost = hours * hourly_rate

                personnel_costs.append(
                    {
                        "employee_id": employee_id,
                        "employee_name": employee["name"],
                        "hours_logged": hours,
                        "hourly_rate": hourly_rate,
                        "cost": cost,
                        "log_date": log.get("logged_date"),
                    }
                )

                total_hours += hours
                total_personnel_cost += cost

        task_expenses = [
            e
            for e in expenses
            if e.get("task_id") == task_id and e.get("status") == "approved"
        ]

        total_expense_cost = sum(e.get("amount", 0) for e in task_expenses)

        story_points = task.get("story_points", 1)
        total_cost = total_personnel_cost + total_expense_cost
        cost_per_point = total_cost / story_points if story_points > 0 else 0

        breakdown = {
            "task_id": task_id,
            "task_title": task["title"],
            "task_status": task["status"],
            "story_points": story_points,
            "cost_breakdown": {
                "personnel_cost": total_personnel_cost,
                "expense_cost": total_expense_cost,
                "total_cost": total_cost,
                "cost_per_story_point": round(cost_per_point, 2),
            },
            "time_metrics": {
                "total_hours_logged": total_hours,
                "average_hourly_cost": (
                    round(total_personnel_cost / total_hours, 2)
                    if total_hours > 0
                    else 0
                ),
                "hours_per_story_point": (
                    round(total_hours / story_points, 2) if story_points > 0 else 0
                ),
            },
            "personnel_details": personnel_costs,
            "expense_count": len(task_expenses),
        }
        payload = breakdown
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetTaskCostBreakdown",
                "description": "Get detailed cost breakdown for a specific task",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "task_id": {"type": "string", "description": "Task ID"}
                    },
                    "required": ["task_id"],
                },
            },
        }
