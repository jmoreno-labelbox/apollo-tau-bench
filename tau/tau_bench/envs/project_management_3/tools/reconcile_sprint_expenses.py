from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime, timezone
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class ReconcileSprintExpenses(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], sprint_id: str = None) -> str:
        if not sprint_id:
            payload = {"error": "sprint_id is required"}
            out = json.dumps(payload)
            return out

        sprints = data.get("sprints", {}).values()
        tasks = data.get("tasks", {}).values()
        task_logs = data.get("task_logs", {}).values()
        expenses = data.get("expenses", {}).values()
        employees = data.get("employees", {}).values()

        sprint = next((s for s in sprints.values() if s.get("sprint_id") == sprint_id), None)
        if not sprint:
            payload = {"error": f"Sprint {sprint_id} not found"}
            out = json.dumps(payload)
            return out

        if sprint.get("status") != "completed":
            payload = {"error": "Can only reconcile completed sprints"}
            out = json.dumps(payload)
            return out

        sprint_tasks = [t for t in tasks.values() if t.get("sprint_id") == sprint_id]

        planned_story_points = sprint.get("planned_story_points", 0)
        completed_story_points = sprint.get("completed_story_points", 0)

        total_hours_logged = 0
        cost_by_employee = {}

        for task in sprint_tasks:
            task_time_logs = [
                log for log in task_logs.values() if log.get("task_id") == task["task_id"]
            ]
            for log in task_time_logs:
                employee_id = log.get("employee_id")
                hours = log.get("hours", 0)
                total_hours_logged += hours

                if employee_id not in cost_by_employee:
                    employee = next(
                        (e for e in employees.values() if e.get("employee_id") == employee_id),
                        None,
                    )
                    if employee:
                        hourly_rate = (
                            150 if "senior" in employee.get("role", "").lower() else 100
                        )
                        cost_by_employee[employee_id] = {
                            "name": employee.get("name"),
                            "hours": 0,
                            "rate": hourly_rate,
                            "cost": 0,
                        }

                cost_by_employee[employee_id]["hours"] += hours
                cost_by_employee[employee_id]["cost"] += (
                    hours * cost_by_employee[employee_id]["rate"]
                )

        from datetime import timezone

        sprint_start = datetime.fromisoformat(
            sprint["start_date"].replace("Z", "+00:00")
        )
        sprint_end = datetime.fromisoformat(sprint["end_date"].replace("Z", "+00:00"))

        sprint_expenses = []
        for expense in expenses.values():
            if expense.get("sprint_id") == sprint_id:
                sprint_data["expenses"][expense["expense_id"]] = expense
            elif expense.get("submitted_date"):

                try:
                    submitted_date = datetime.fromisoformat(
                        expense["submitted_date"].replace("Z", "+00:00")
                    )
                    if sprint_start <= submitted_date <= sprint_end:
                        sprint_data["expenses"][expense["expense_id"]] = expense
                except:

                    pass

        total_expense_amount = sum(
            e.get("amount", 0) for e in sprint_expenses if e.get("status") == "approved"
        )

        estimated_hours = planned_story_points * 6
        hour_variance = (
            ((total_hours_logged - estimated_hours) / estimated_hours * 100)
            if estimated_hours > 0
            else 0
        )

        total_personnel_cost = sum(emp["cost"] for emp in cost_by_employee.values())

        reconciliation = {
            "sprint_id": sprint_id,
            "sprint_name": sprint.get("sprint_name"),
            "team_id": sprint.get("team_id"),
            "performance_metrics": {
                "planned_story_points": planned_story_points,
                "completed_story_points": completed_story_points,
                "completion_rate": (
                    round((completed_story_points / planned_story_points * 100), 2)
                    if planned_story_points > 0
                    else 0
                ),
            },
            "cost_metrics": {
                "total_hours_logged": total_hours_logged,
                "estimated_hours": estimated_hours,
                "hour_variance_percentage": round(hour_variance, 2),
                "personnel_cost": total_personnel_cost,
                "expense_cost": total_expense_amount,
                "total_cost": total_personnel_cost + total_expense_amount,
                "cost_per_story_point": (
                    round(
                        (total_personnel_cost + total_expense_amount)
                        / completed_story_points,
                        2,
                    )
                    if completed_story_points > 0
                    else 0
                ),
            },
            "employee_breakdown": list(cost_by_employee.values()),
            "expense_count": len(sprint_expenses),
            "reconciliation_date": datetime.now(timezone.utc).isoformat(),
        }

        if hour_variance > 20:
            reconciliation["recommendations"] = [
                "Review estimation practices - significant overrun detected"
            ]
        elif hour_variance < -20:
            reconciliation["recommendations"] = [
                "Team may be over-estimating - consider adjusting story point values"
            ]
        payload = reconciliation
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ReconcileSprintExpenses",
                "description": "Reconcile sprint expenses with actual hours logged and story points completed",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "sprint_id": {
                            "type": "string",
                            "description": "Sprint ID to reconcile",
                        }
                    },
                    "required": ["sprint_id"],
                },
            },
        }
