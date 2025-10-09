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

class UpdateTaskPriority(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], task_id: str = None, new_priority: str = None) -> str:
        if not all([task_id, new_priority]):
            payload = {"error": "task_id and new_priority are required"}
            out = json.dumps(payload)
            return out

        if new_priority not in ["low", "medium", "high", "critical"]:
            payload = {"error": "Priority must be one of: low, medium, high, critical"}
            out = json.dumps(payload)
            return out

        tasks = data.get("tasks", {}).values()
        task_history = data.get("task_history", {}).values()
        employees = data.get("employees", {}).values()

        task = next((t for t in tasks.values() if t.get("task_id") == task_id), None)
        if not task:
            payload = {"error": f"Task '{task_id}' not found"}
            out = json.dumps(payload)
            return out

        old_priority = task.get("priority")

        if new_priority == "critical" and old_priority != "critical":
            assignee = next(
                (
                    emp
                    for emp in employees.values() if emp.get("employee_id") == task.get("assignee_id")
                ),
                None,
            )
            if assignee:
                is_senior = any(
                    skill.get("proficiency", 0) >= 4
                    for skill in assignee.get("skills", [])
                )
                if not is_senior:
                    senior_members = [
                        emp
                        for emp in employees.values() if any(
                            skill.get("proficiency", 0) >= 4
                            for skill in emp.get("skills", [])
                        )
                    ]
                    if senior_members:
                        payload = {
                            "error": "Critical tasks must be assigned to senior team members",
                            "current_assignee": assignee.get("name"),
                            "needs_reassignment": True,
                            "available_seniors": [
                                {"id": emp["employee_id"], "name": emp["name"]}
                                for emp in senior_members[:5]
                            ],
                        }
                        out = json.dumps(payload)
                        return out

        history_entry = {
            "history_id": f"hist_{uuid.uuid4().hex[:8]}",
            "task_id": task_id,
            "action": "priority_changed",
            "from_priority": old_priority,
            "to_priority": new_priority,
            "timestamp": datetime.now().isoformat(),
        }
        data["task_history"][history_entry["task_history_id"]] = history_entry

        task["priority"] = new_priority
        task["updated_date"] = datetime.now().isoformat()
        payload = {
            "success": True,
            "task": task,
            "priority_change": f"{old_priority} -> {new_priority}",
        }
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateTaskPriority",
                "description": "Update the priority of a task",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "task_id": {
                            "type": "string",
                            "description": "The task ID to update",
                        },
                        "new_priority": {
                            "type": "string",
                            "description": "New priority: low, medium, high, critical",
                        },
                    },
                    "required": ["task_id", "new_priority"],
                },
            },
        }
