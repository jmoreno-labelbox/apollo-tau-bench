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

class ValidateExpenseSubmission(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        employee_id: str = None,
        project_id: str = None,
        amount: float = None,
        expense_date: str = None,
        category: str = None,
        sprint_id: str = None,
        task_id: str = None
    ) -> str:
        if not all([employee_id, project_id, amount, category]):
            payload = {"error": "employee_id, project_id, amount, and category are required"}
            out = json.dumps(payload)
            return out

        allocations = data.get("allocations", {}).values()
        projects = data.get("projects", {}).values()
        sprints = data.get("sprints", {}).values()
        tasks = data.get("tasks", {}).values()

        project = next((p for p in projects.values() if p.get("project_id") == project_id), None)
        if not project:
            payload = {"error": f"Project {project_id} not found"}
            out = json.dumps(payload)
            return out

        if project.get("status") in ["cancelled", "completed"]:
            payload = {"error": f"Cannot submit expense for {project.get('status')} project"}
            out = json.dumps(payload)
            return out

        employee_allocation = next(
            (
                a
                for a in allocations.values() if a.get("employee_id") == employee_id
                and a.get("project_id") == project_id
                and a.get("status") == "active"
            ),
            None,
        )

        if not employee_allocation:
            payload = {
                "error": f"Employee {employee_id} is not allocated to project {project_id}"
            }
            out = json.dumps(payload)
            return out

        allocation_percentage = employee_allocation.get("hours_per_week", 0) / 40
        base_limit = 1000
        adjusted_limit = base_limit * allocation_percentage

        validation_result = {
            "valid": True,
            "employee_id": employee_id,
            "project_id": project_id,
            "allocation_percentage": round(allocation_percentage * 100, 1),
            "reimbursement_limit": adjusted_limit,
            "warnings": [],
        }

        if sprint_id:
            sprint = next((s for s in sprints.values() if s.get("sprint_id") == sprint_id), None)
            if sprint:
                if sprint.get("status") != "active":
                    validation_result["warnings"].append(
                        f"Sprint {sprint_id} is not active"
                    )

                if expense_date:
                    expense_dt = datetime.fromisoformat(
                        expense_date.replace("Z", "+00:00")
                    )
                    sprint_start = datetime.fromisoformat(
                        sprint["start_date"].replace("Z", "+00:00")
                    )
                    sprint_end = datetime.fromisoformat(
                        sprint["end_date"].replace("Z", "+00:00")
                    )

                    if not (
                        sprint_start.timestamp()
                        <= expense_dt.timestamp()
                        <= sprint_end.timestamp()
                    ):
                        validation_result["warnings"].append(
                            "Expense date is outside sprint duration"
                        )

        if task_id:
            task = next((t for t in tasks.values() if t.get("task_id") == task_id), None)
            if task:
                if task.get("assignee_id") != employee_id:
                    validation_result["valid"] = False
                    validation_result["error"] = (
                        f"Task {task_id} is not assigned to employee {employee_id}"
                    )
                elif task.get("status") == "todo":
                    validation_result["warnings"].append(
                        "Task has not been started yet"
                    )

        if amount > adjusted_limit:
            validation_result["warnings"].append(
                f"Amount exceeds adjusted limit of ${adjusted_limit}"
            )
        payload = validation_result
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ValidateExpenseSubmission",
                "description": "Validate expense submission against employee allocation and project rules",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "employee_id": {"type": "string", "description": "Employee ID"},
                        "project_id": {"type": "string", "description": "Project ID"},
                        "amount": {"type": "number", "description": "Expense amount"},
                        "expense_date": {
                            "type": "string",
                            "description": "Date of expense",
                        },
                        "category": {
                            "type": "string",
                            "description": "Expense category",
                        },
                        "sprint_id": {
                            "type": "string",
                            "description": "Associated sprint ID",
                        },
                        "task_id": {
                            "type": "string",
                            "description": "Associated task ID",
                        },
                    },
                    "required": ["employee_id", "project_id", "amount", "category"],
                },
            },
        }
