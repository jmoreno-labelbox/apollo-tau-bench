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

class AllocateTaskExpenses(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        task_id: str = None,
        expense_amount: float = None,
        expense_category: str = None,
        description: str = None
    ) -> str:
        if not all([task_id, expense_amount, expense_category, description]):
            payload = {"error": "All fields are required"}
            out = json.dumps(payload)
            return out

        tasks = data.get("tasks", [])
        expenses = data.get("expenses", [])
        allocations = data.get("allocations", [])
        budgets = data.get("budgets", [])

        task = next((t for t in tasks if t.get("task_id") == task_id), None)
        if not task:
            payload = {"error": f"Task {task_id} not found"}
            out = json.dumps(payload)
            return out

        employee_id = task.get("assignee_id")
        employee_allocation = next(
            (
                a
                for a in allocations
                if a.get("employee_id") == employee_id and a.get("status") == "active"
            ),
            None,
        )

        if not employee_allocation:
            payload = {"error": "Cannot determine project for task expense"}
            out = json.dumps(payload)
            return out

        project_id = employee_allocation.get("project_id")

        if task.get("status") not in ["in_progress", "done"]:
            payload = {"error": "Expenses can only be allocated to active or completed tasks"}
            out = json.dumps(payload)
            return out

        expense_id = f"exp_{uuid.uuid4().hex[:8]}"

        from datetime import timezone

        current_time = datetime.now(timezone.utc)

        new_expense = {
            "expense_id": expense_id,
            "project_id": project_id,
            "task_id": task_id,
            "sprint_id": task.get("sprint_id"),
            "amount": expense_amount,
            "category": expense_category,
            "description": description,
            "employee_id": employee_id,
            "status": "approved",
            "submitted_date": current_time.isoformat(),
            "fiscal_year": current_time.year,
            "task_details": {
                "task_title": task.get("title"),
                "task_status": task.get("status"),
                "story_points": task.get("story_points"),
                "time_logged": task.get("time_logged", 0),
            },
        }

        expenses.append(new_expense)

        budget = next(
            (
                b
                for b in budgets
                if b.get("project_id") == project_id
                and b.get("fiscal_year") == current_time.year
            ),
            None,
        )

        if budget:
            budget["spent_amount"] = budget.get("spent_amount", 0) + expense_amount
            budget["last_modified"] = current_time.isoformat()

        cost_per_point = expense_amount / task.get("story_points", 1)
        payload = {
            "success": True,
            "expense": new_expense,
            "cost_per_story_point": round(cost_per_point, 2),
        }
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AllocateTaskExpenses",
                "description": "Allocate expenses directly to specific tasks",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "task_id": {"type": "string", "description": "Task ID"},
                        "expense_amount": {
                            "type": "number",
                            "description": "Expense amount",
                        },
                        "expense_category": {
                            "type": "string",
                            "description": "Expense category",
                        },
                        "description": {
                            "type": "string",
                            "description": "Expense description",
                        },
                    },
                    "required": [
                        "task_id",
                        "expense_amount",
                        "expense_category",
                        "description",
                    ],
                },
            },
        }
