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

class GetEmployeeCostByProject(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any], 
        employee_id: str = None, 
        project_id: str = None, 
        include_expenses: bool = True
    ) -> str:
        if not all([employee_id, project_id]):
            payload = {"error": "employee_id and project_id are required"}
            out = json.dumps(payload)
            return out

        employees = data.get("employees", [])
        allocations = data.get("allocations", [])
        task_logs = data.get("task_logs", [])
        tasks = data.get("tasks", [])
        expenses = data.get("expenses", [])

        employee = next(
            (e for e in employees if e.get("employee_id") == employee_id), None
        )
        if not employee:
            payload = {"error": f"Employee {employee_id} not found"}
            out = json.dumps(payload)
            return out

        project_allocation = next(
            (
                a
                for a in allocations
                if a.get("employee_id") == employee_id
                and a.get("project_id") == project_id
            ),
            None,
        )

        hourly_rate = 150 if "senior" in employee.get("role", "").lower() else 100

        employee_project_tasks = [
            t
            for t in tasks
            if t.get("assignee_id") == employee_id
            and any(
                a.get("project_id") == project_id
                for a in allocations
                if a.get("employee_id") == employee_id
            )
        ]

        total_hours = 0
        task_details = []

        for task in employee_project_tasks:
            task_time_logs = [
                log
                for log in task_logs
                if log.get("task_id") == task["task_id"]
                and log.get("employee_id") == employee_id
            ]

            task_hours = sum(log.get("hours", 0) for log in task_time_logs)
            total_hours += task_hours

            if task_hours > 0:
                task_details.append(
                    {
                        "task_id": task["task_id"],
                        "task_title": task["title"],
                        "hours_logged": task_hours,
                        "cost": task_hours * hourly_rate,
                    }
                )

        total_time_cost = total_hours * hourly_rate

        employee_expenses = []
        total_expense_amount = 0

        if include_expenses:
            employee_expenses = [
                e
                for e in expenses
                if e.get("employee_id") == employee_id
                and e.get("project_id") == project_id
                and e.get("status") == "approved"
            ]
            total_expense_amount = sum(e.get("amount", 0) for e in employee_expenses)

        employee_cost = {
            "employee_id": employee_id,
            "employee_name": employee["name"],
            "project_id": project_id,
            "allocation_status": "active" if project_allocation else "inactive",
            "cost_summary": {
                "total_hours_logged": total_hours,
                "hourly_rate": hourly_rate,
                "time_based_cost": total_time_cost,
                "expense_cost": total_expense_amount,
                "total_cost": total_time_cost + total_expense_amount,
            },
            "tasks_worked": len(task_details),
            "task_details": task_details[:10],
            "expense_count": len(employee_expenses) if include_expenses else None,
        }

        if project_allocation:
            employee_cost["allocation_details"] = {
                "hours_per_week": project_allocation.get("hours_per_week", 0),
                "role": project_allocation.get("role"),
                "start_date": project_allocation.get("start_date"),
                "end_date": project_allocation.get("end_date"),
            }
        payload = employee_cost
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetEmployeeCostByProject",
                "description": "Get total cost incurred by an employee on a specific project",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "employee_id": {"type": "string", "description": "Employee ID"},
                        "project_id": {"type": "string", "description": "Project ID"},
                        "include_expenses": {
                            "type": "boolean",
                            "description": "Include expense data",
                        },
                    },
                    "required": ["employee_id", "project_id"],
                },
            },
        }
