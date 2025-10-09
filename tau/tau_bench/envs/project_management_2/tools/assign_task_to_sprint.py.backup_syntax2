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

class AssignTaskToSprint(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], task_id: str = None, sprint_id: str = None) -> str:
        if not all([task_id, sprint_id]):
            payload = {"error": "task_id and sprint_id are required"}
            out = json.dumps(payload)
            return out

        tasks = data.get("tasks", {}).values()
        sprints = data.get("sprints", {}).values()
        teams = data.get("teams", {}).values()

        task = next((t for t in tasks.values() if t.get("task_id") == task_id), None)
        sprint = next((s for s in sprints.values() if s.get("sprint_id") == sprint_id), None)

        if not task:
            payload = {"error": f"Task '{task_id}' not found"}
            out = json.dumps(payload)
            return out
        if not sprint:
            payload = {"error": f"Sprint '{sprint_id}' not found"}
            out = json.dumps(payload)
            return out

        if sprint.get("status") not in ["planning", "active"]:
            payload = {
                    "error": f"Cannot add tasks to sprint in '{sprint.get('status')}' status"
                }
            out = json.dumps(
                payload)
            return out

        if sprint.get("status") == "active" and task.get("priority") != "critical":
            payload = {
                    "error": "Cannot add non-critical tasks to active sprint",
                }
            out = json.dumps(
                payload)
            return out

        team = next(
            (t for t in teams.values() if t.get("team_id") == sprint.get("team_id")), None
        )
        if team:

            team_members = team.get("members", [])

            completed_sprints = [
                s
                for s in sprints.values() if s.get("team_id") == team.get("team_id")
                and s.get("status") == "completed"
            ]

            if len(completed_sprints) >= 3:

                recent_sprints = sorted(
                    completed_sprints, key=lambda x: x.get("end_date", ""), reverse=True
                )[:3]
                avg_velocity = sum(s.get("velocity", 0) for s in recent_sprints.values() / 3
                capacity_limit = avg_velocity * 0.8
            else:

                capacity_limit = len(team_members) * 20

            sprint_tasks = [t for t in tasks.values() if t.get("sprint_id") == sprint_id]
            current_points = sum(t.get("story_points", 0) for t in sprint_tasks.values()
            new_total = current_points + task.get("story_points", 0)

            if new_total > capacity_limit:
                payload = {
                        "error": "Adding task would exceed sprint capacity limit",
                        "current_points": current_points,
                        "task_points": task.get("story_points", 0),
                        "total_would_be": new_total,
                        "capacity_limit": capacity_limit,
                    }
                out = json.dumps(
                    payload)
                return out

            assignee_sprint_tasks = [
                t
                for t in sprint_tasks
                if t.get("assignee_id") == task.get("assignee_id")
            ]
            assignee_points = sum(
                t.get("story_points", 0) for t in assignee_sprint_tasks
            )

            if assignee_points + task.get("story_points", 0) > 25:
                payload = {
                        "error": f"Cannot assign task. Would exceed 25 story point limit for {task.get('assignee_id')}",
                        "current_points": assignee_points,
                        "task_points": task.get("story_points", 0),
                        "total_would_be": assignee_points + task.get("story_points", 0),
                    }
                out = json.dumps(
                    payload)
                return out

        task["sprint_id"] = sprint_id
        task["updated_date"] = datetime.now().isoformat()

        sprint["planned_story_points"] = sprint.get(
            "planned_story_points", 0
        ) + task.get("story_points", 0)
        payload = {
                "success": True,
                "task": task,
                "sprint_planned_points": sprint["planned_story_points"],
            }
        out = json.dumps(
            payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AssignTaskToSprint",
                "description": "Assign a task to a sprint",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "task_id": {
                            "type": "string",
                            "description": "The task ID to assign",
                        },
                        "sprint_id": {
                            "type": "string",
                            "description": "The sprint ID to assign to",
                        },
                    },
                    "required": ["task_id", "sprint_id"],
                },
            },
        }
