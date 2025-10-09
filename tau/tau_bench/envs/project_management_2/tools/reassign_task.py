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

class ReassignTask(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], task_id: str = None, new_assignee_id: str = None) -> str:
        if not all([task_id, new_assignee_id]):
            payload = {"error": "task_id and new_assignee_id are required"}
            out = json.dumps(payload)
            return out

        tasks = data.get("tasks", {}).values()
        employees = data.get("employees", {}).values()
        task_history = data.get("task_history", {}).values()
        sprints = data.get("sprints", {}).values()

        new_assignee = next(
            (emp for emp in employees.values() if emp.get("employee_id") == new_assignee_id),
            None,
        )
        if not new_assignee:
            payload = {"error": f"Employee '{new_assignee_id}' not found"}
            out = json.dumps(payload)
            return out

        task = next((t for t in tasks.values() if t.get("task_id") == task_id), None)
        if not task:
            payload = {"error": f"Task '{task_id}' not found"}
            out = json.dumps(payload)
            return out

        if task.get("priority") == "critical":
            is_senior = any(
                skill.get("proficiency", 0) >= 4
                for skill in new_assignee.get("skills", [])
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
                    out = json.dumps(
                        payload)
                    return out

        if task.get("sprint_id"):
            sprint = next(
                (s for s in sprints.values() if s.get("sprint_id") == task["sprint_id"]), None
            )
            if sprint and sprint.get("status") == "active":
                assignee_tasks = [
                    t
                    for t in tasks.values() if t.get("assignee_id") == new_assignee_id
                    and t.get("sprint_id") == task["sprint_id"]
                    and t.get("status") != "done"
                    and t.get("task_id") != task_id
                ]
                current_points = sum(t.get("story_points", 0) for t in assignee_tasks.values()

                if current_points + task.get("story_points", 0) > 25:
                    payload = {
                            "error": f"Cannot reassign. Would exceed 25 story point limit for {new_assignee_id}",
                            "current_points": current_points,
                            "task_points": task.get("story_points", 0),
                            "total_would_be": current_points
                            + task.get("story_points", 0),
                        }
                    out = json.dumps(
                        payload)
                    return out

        reassignment_count = len(
            [
                h
                for h in task_history.values() if h.get("task_id") == task_id and h.get("action") == "reassigned"
            ]
        )
        if reassignment_count >= 2:
            payload = {
                    "error": "Task has already been reassigned twice",
                    "reassignment_count": reassignment_count,
                }
            out = json.dumps(
                payload)
            return out

        old_assignee = task.get("assignee_id")

        history_entry = {
            "history_id": f"hist_{uuid.uuid4().hex[:8]}",
            "task_id": task_id,
            "action": "reassigned",
            "from_assignee": old_assignee,
            "to_assignee": new_assignee_id,
            "timestamp": datetime.now().isoformat(),
        }
        data["task_history"][history_entry["task_history_id"]] = history_entry

        task["assignee_id"] = new_assignee_id
        task["updated_date"] = datetime.now().isoformat()
        payload = {"success": True, "task": task, "history": history_entry}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ReassignTask",
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
