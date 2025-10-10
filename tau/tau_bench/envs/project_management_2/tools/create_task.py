# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateTask(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        new_task_id = kwargs.get("new_task_id")
        title = kwargs.get("title")
        description = kwargs.get("description")
        assignee_id = kwargs.get("assignee_id")
        priority = kwargs.get("priority", "medium")
        story_points = kwargs.get("story_points", 3)
        sprint_id = kwargs.get("sprint_id")
        dependencies = kwargs.get("dependencies", [])

        if not all([title, assignee_id]):
            return json.dumps({"error": "title and assignee_id are required"})

        tasks = list(data.get("tasks", {}).values())
        employees = list(data.get("employees", {}).values())
        sprints = data.get("sprints", [])

        assignee = next(
            (emp for emp in employees if emp.get("employee_id") == assignee_id), None
        )
        if not assignee:
            return json.dumps({"error": f"Employee '{assignee_id}' not found"})

        if priority == "critical":

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
                            "error": "Critical tasks must be assigned to senior team members (proficiency 4+)",
                            "available_seniors": [
                                {"id": emp["employee_id"], "name": emp["name"]}
                                for emp in senior_members[:5]
                            ],
                        }
                    )

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
                            "error": f"Cannot assign task. Would exceed 25 story point limit for {assignee_id}",
                            "current_points": current_points,
                            "new_task_points": story_points,
                            "total_would_be": current_points + story_points,
                        }
                    )

        for dep_id in dependencies:
            if not any(task.get("task_id") == dep_id for task in tasks):
                return json.dumps({"error": f"Dependency task '{dep_id}' not found"})

        task_id = f"task_{uuid.uuid4().hex[:8]}"

        if new_task_id:
            for t in tasks:
                if t.get("task_id") == new_task_id:
                    return json.dumps({"error": f"new_task_id {new_task_id} exists. Please enter a unique task_id."})
            task_id = new_task_id

        new_task = {
            "task_id": task_id,
            "title": title,
            "description": description,
            "assignee_id": assignee_id,
            "status": "todo",
            "priority": priority,
            "story_points": story_points,
            "sprint_id": sprint_id,
            "dependencies": dependencies,
            "blocked_by": [],
            "created_date": datetime.now().isoformat(),
            "updated_date": datetime.now().isoformat(),
            "completed_date": None,
            "time_logged": 0,
        }

        tasks.append(new_task)

        return json.dumps({"success": True, "task": new_task})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_task",
                "description": "Create a new task with optional dependencies",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "title": {"type": "string", "description": "Task title"},
                        "description": {
                            "type": "string",
                            "description": "Detailed task description",
                        },
                        "assignee_id": {
                            "type": "string",
                            "description": "Employee ID to assign the task to",
                        },
                        "priority": {
                            "type": "string",
                            "description": "Priority level: low, medium, high, critical",
                        },
                        "story_points": {
                            "type": "integer",
                            "description": "Estimated story points (1-13)",
                        },
                        "sprint_id": {
                            "type": "string",
                            "description": "Sprint to assign task to (optional)",
                        },
                        "dependencies": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of task IDs this task depends on",
                        },
                    },
                    "required": ["title", "assignee_id"],
                },
            },
        }
