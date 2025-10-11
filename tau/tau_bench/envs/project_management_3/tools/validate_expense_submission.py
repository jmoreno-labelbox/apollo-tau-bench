# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ValidateExpenseSubmission(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], amount, category, employee_id, expense_date, project_id, sprint_id, task_id) -> str:

        if not all([employee_id, project_id, amount, category]):
            return json.dumps(
                {"error": "employee_id, project_id, amount, and category are required"}
            )

        allocations = data.get("allocations", [])
        projects = list(data.get("projects", {}).values())
        sprints = data.get("sprints", [])
        tasks = list(data.get("tasks", {}).values())

        project = next((p for p in projects if p.get("project_id") == project_id), None)
        if not project:
            return json.dumps({"error": f"Project {project_id} not found"})

        if project.get("status") in ["cancelled", "completed"]:
            return json.dumps(
                {"error": f"Cannot submit expense for {project.get('status')} project"}
            )

        employee_allocation = next(
            (
                a
                for a in allocations
                if a.get("employee_id") == employee_id
                and a.get("project_id") == project_id
                and a.get("status") == "active"
            ),
            None,
        )

        if not employee_allocation:
            return json.dumps(
                {
                    "error": f"Employee {employee_id} is not allocated to project {project_id}"
                }
            )

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
            sprint = next((s for s in sprints if s.get("sprint_id") == sprint_id), None)
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

                    if not (sprint_start.timestamp() <= expense_dt.timestamp() <= sprint_end.timestamp()):
                        validation_result["warnings"].append(
                            "Expense date is outside sprint duration"
                        )

        if task_id := task_id:
            task = next((t for t in tasks if t.get("task_id") == task_id), None)
            if task:
                if task.get("assignee_id") != employee_id:
                    validation_result["valid"] = False
                    validation_result[
                        "error"
                    ] = f"Task {task_id} is not assigned to employee {employee_id}"
                elif task.get("status") == "todo":
                    validation_result["warnings"].append(
                        "Task has not been started yet"
                    )

        if amount > adjusted_limit:
            validation_result["warnings"].append(
                f"Amount exceeds adjusted limit of ${adjusted_limit}"
            )

        return json.dumps(validation_result, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "validate_expense_submission",
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
