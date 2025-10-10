# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateTaskPriority(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        task_id = kwargs.get("task_id")
        new_priority = kwargs.get("new_priority")

        if not all([task_id, new_priority]):
            return json.dumps({"error": "task_id and new_priority are required"})

        if new_priority not in ["low", "medium", "high", "critical"]:
            return json.dumps(
                {"error": "Priority must be one of: low, medium, high, critical"}
            )

        tasks = list(data.get("tasks", {}).values())
        task_history = list(data.get("task_history", {}).values())
        employees = list(data.get("employees", {}).values())

        task = next((t for t in tasks if t.get("task_id") == task_id), None)
        if not task:
            return json.dumps({"error": f"Task '{task_id}' not found"})

        old_priority = task.get("priority")

        if new_priority == "critical" and old_priority != "critical":
            assignee = next(
                (
                    emp
                    for emp in employees
                    if emp.get("employee_id") == task.get("assignee_id")
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
                        for emp in employees
                        if any(
                            skill.get("proficiency", 0) >= 4
                            for skill in emp.get("skills", [])
                        )
                    ]
                    if senior_members:
                        return json.dumps(
                            {
                                "error": "Critical tasks must be assigned to senior team members",
                                "current_assignee": assignee.get("name"),
                                "needs_reassignment": True,
                                "available_seniors": [
                                    {"id": emp["employee_id"], "name": emp["name"]}
                                    for emp in senior_members[:5]
                                ],
                            }
                        )

        history_entry = {
            "history_id": f"hist_{uuid.uuid4().hex[:8]}",
            "task_id": task_id,
            "action": "priority_changed",
            "from_priority": old_priority,
            "to_priority": new_priority,
            "timestamp": datetime.now().isoformat(),
        }
        task_history.append(history_entry)

        task["priority"] = new_priority
        task["updated_date"] = datetime.now().isoformat()

        return json.dumps(
            {
                "success": True,
                "task": task,
                "priority_change": f"{old_priority} -> {new_priority}",
            }
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_task_priority",
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
