# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CloneTask(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        source_task_id = kwargs.get("source_task_id")
        new_title = kwargs.get("new_title")
        new_assignee_id = kwargs.get("new_assignee_id")
        sprint_id = kwargs.get("sprint_id")
        new_task_id = kwargs.get("new_task_id")

        if not all([source_task_id, new_title]):
            return json.dumps({"error": "source_task_id and new_title are required"})

        tasks = list(data.get("tasks", {}).values())
        employees = list(data.get("employees", {}).values())
        sprints = data.get("sprints", [])

        source_task = next(
            (t for t in tasks if t.get("task_id") == source_task_id), None
        )
        if not source_task:
            return json.dumps({"error": f"Source task '{source_task_id}' not found"})

        assignee_id = new_assignee_id or source_task.get("assignee_id")

        assignee = next(
            (emp for emp in employees if emp.get("employee_id") == assignee_id), None
        )
        if not assignee:
            return json.dumps({"error": f"Assignee '{assignee_id}' not found"})

        if source_task.get("priority") == "critical":
            is_senior = any(
                skill.get("proficiency", 0) >= 4 for skill in assignee.get("skills", [])
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
                            "available_seniors": [
                                {"id": emp["employee_id"], "name": emp["name"]}
                                for emp in senior_members[:5]
                            ],
                        }
                    )

        story_points = source_task.get("story_points", 3)
        if sprint_id:
            sprint = next((s for s in sprints if s.get("sprint_id") == sprint_id), None)
            if sprint and sprint.get("status") == "active":
                assignee_tasks = [
                    t
                    for t in tasks
                    if t.get("assignee_id") == assignee_id
                    and t.get("sprint_id") == sprint_id
                    and t.get("status") != "done"
                ]
                current_points = sum(t.get("story_points", 0) for t in assignee_tasks)

                if current_points + story_points > 25:
                    return json.dumps(
                        {
                            "error": f"Cannot assign task. Would exceed 25 story point limit",
                            "current_points": current_points,
                            "new_task_points": story_points,
                        }
                    )

        task_id = f"task_{uuid.uuid4().hex[:8]}"

        if new_task_id:
            for t in tasks:
                if t.get("task_id") == new_task_id:
                    return json.dumps({"error": f"new_task_id {new_task_id} exists. Please enter a unique task_id."})
            task_id = new_task_id

        new_task = {
            "task_id": task_id,
            "title": new_title,
            "description": source_task.get("description", ""),
            "assignee_id": assignee_id,
            "status": "todo",
            "priority": source_task.get("priority", "medium"),
            "story_points": story_points,
            "sprint_id": sprint_id,
            "dependencies": [],
            "blocked_by": [],
            "created_date": datetime.now().isoformat(),
            "updated_date": datetime.now().isoformat(),
            "completed_date": None,
            "time_logged": 0,
            "cloned_from": source_task_id,
        }

        tasks.append(new_task)

        return json.dumps(
            {"success": True, "new_task": new_task, "source_task_id": source_task_id}
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "clone_task",
                "description": "Create a copy of an existing task",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "source_task_id": {
                            "type": "string",
                            "description": "Task ID to clone from",
                        },
                        "new_title": {
                            "type": "string",
                            "description": "Title for the new task",
                        },
                        "new_assignee_id": {
                            "type": "string",
                            "description": "Optional new assignee (defaults to source task assignee)",
                        },
                        "sprint_id": {
                            "type": "string",
                            "description": "Optional sprint to assign to",
                        },
                        "new_task_id": {
                            "type": "string",
                            "description": "Optional task_id",
                        },
                    },
                    "required": ["source_task_id", "new_title"],
                },
            },
        }
