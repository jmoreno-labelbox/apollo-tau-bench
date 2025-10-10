# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ReassignTask(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        task_id = kwargs.get("task_id")
        new_assignee_id = kwargs.get("new_assignee_id")

        if not all([task_id, new_assignee_id]):
            return json.dumps({"error": "task_id and new_assignee_id are required"})

        tasks = list(data.get("tasks", {}).values())
        employees = list(data.get("employees", {}).values())
        task_history = data.get("task_history", [])
        sprints = data.get("sprints", [])

        new_assignee = next(
            (emp for emp in employees if emp.get("employee_id") == new_assignee_id),
            None,
        )
        if not new_assignee:
            return json.dumps({"error": f"Employee '{new_assignee_id}' not found"})

        task = next((t for t in tasks if t.get("task_id") == task_id), None)
        if not task:
            return json.dumps({"error": f"Task '{task_id}' not found"})

        if task.get("priority") == "critical":
            is_senior = any(
                skill.get("proficiency", 0) >= 4
                for skill in new_assignee.get("skills", [])
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
                            "error": "Critical tasks must be assigned to senior team members (proficiency 4+)",
                            "available_seniors": [
                                {"id": emp["employee_id"], "name": emp["name"]}
                                for emp in senior_members[:5]
                            ],
                        }
                    )

        if task.get("sprint_id"):
            sprint = next(
                (s for s in sprints if s.get("sprint_id") == task["sprint_id"]), None
            )
            if sprint and sprint.get("status") == "active":
                assignee_tasks = [
                    t
                    for t in tasks
                    if t.get("assignee_id") == new_assignee_id
                    and t.get("sprint_id") == task["sprint_id"]
                    and t.get("status") != "done"
                    and t.get("task_id") != task_id
                ]
                current_points = sum(t.get("story_points", 0) for t in assignee_tasks)

                if current_points + task.get("story_points", 0) > 25:
                    return json.dumps(
                        {
                            "error": f"Cannot reassign. Would exceed 25 story point limit for {new_assignee_id}",
                            "current_points": current_points,
                            "task_points": task.get("story_points", 0),
                            "total_would_be": current_points
                            + task.get("story_points", 0),
                        }
                    )

        reassignment_count = len(
            [
                h
                for h in task_history
                if h.get("task_id") == task_id and h.get("action") == "reassigned"
            ]
        )
        if reassignment_count >= 2:
            return json.dumps(
                {
                    "error": "Task has already been reassigned twice",
                    "reassignment_count": reassignment_count,
                }
            )

        old_assignee = task.get("assignee_id")

        history_entry = {
            "history_id": f"hist_{uuid.uuid4().hex[:8]}",
            "task_id": task_id,
            "action": "reassigned",
            "from_assignee": old_assignee,
            "to_assignee": new_assignee_id,
            "timestamp": datetime.now().isoformat(),
        }
        task_history.append(history_entry)

        task["assignee_id"] = new_assignee_id
        task["updated_date"] = datetime.now().isoformat()

        return json.dumps({"success": True, "task": task, "history": history_entry})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "reassign_task",
                "description": "Reassign a task to a different team member",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "task_id": {
                            "type": "string",
                            "description": "The task ID to reassign",
                        },
                        "new_assignee_id": {
                            "type": "string",
                            "description": "The new assignee's employee ID",
                        },
                    },
                    "required": ["task_id", "new_assignee_id"],
                },
            },
        }
