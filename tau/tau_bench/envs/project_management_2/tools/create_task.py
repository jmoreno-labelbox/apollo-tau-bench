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

class CreateTask(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        new_task_id: str = None,
        title: str = None,
        description: str = None,
        assignee_id: str = None,
        priority: str = "medium",
        story_points: int = 3,
        sprint_id: str = None,
        dependencies: list = None,
    ) -> str:
        if dependencies is None:
            dependencies = []

        if not all([title, assignee_id]):
            payload = {"error": "title and assignee_id are required"}
            out = json.dumps(payload)
            return out

        tasks = data.get("tasks", {}).values()
        employees = data.get("employees", {}).values()
        sprints = data.get("sprints", {}).values()

        assignee = next(
            (emp for emp in employees.values() if emp.get("employee_id") == assignee_id), None
        )
        if not assignee:
            payload = {"error": f"Employee '{assignee_id}' not found"}
            out = json.dumps(payload)
            return out

        if priority == "critical":
            is_senior = any(
                skill.get("proficiency", 0) >= 4 for skill in assignee.get("skills", [])
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
                        "error": "Critical tasks must be assigned to senior team members (proficiency 4+)",
                        "available_seniors": [
                            {"id": emp["employee_id"], "name": emp["name"]}
                            for emp in senior_members[:5]
                        ],
                    }
                    out = json.dumps(payload)
                    return out

        if sprint_id:
            sprint = next((s for s in sprints.values() if s.get("sprint_id") == sprint_id), None)
            if sprint and sprint.get("status") == "active":
                assignee_tasks = [
                    t
                    for t in tasks.values() if t.get("assignee_id") == assignee_id
                    and t.get("sprint_id") == sprint_id
                    and t.get("status") != "done"
                ]
                current_points = sum(t.get("story_points", 0) for t in assignee_tasks.values())

                if current_points + story_points > 25:
                    payload = {
                        "error": f"Cannot assign task. Would exceed 25 story point limit for {assignee_id}",
                        "current_points": current_points,
                        "new_task_points": story_points,
                        "total_would_be": current_points + story_points,
                    }
                    out = json.dumps(payload)
                    return out

        for dep_id in dependencies:
            if not any(task.get("task_id") == dep_id for task in tasks.values()):
                payload = {"error": f"Dependency task '{dep_id}' not found"}
                out = json.dumps(payload)
                return out

        task_id = f"task_{uuid.uuid4().hex[:8]}"

        if new_task_id:
            for t in tasks.values():
                if t.get("task_id") == new_task_id:
                    payload = {
                        "error": f"new_task_id {new_task_id} exists. Please enter a unique task_id."
                    }
                    out = json.dumps(payload)
                    return out
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

        data["tasks"][task_id] = new_task
        payload = {"success": True, "task": new_task}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateTask",
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
