# Copyright Sierra

import datetime
import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class AssignTaskToSprint(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], sprint_id, task_id) -> str:

        if not all([task_id, sprint_id]):
            return json.dumps({"error": "task_id and sprint_id are required"})

        tasks = list(data.get("tasks", {}).values())
        sprints = list(data.get("sprints", {}).values())
        teams = list(data.get("teams", {}).values())

        task = next((t for t in tasks if t.get("task_id") == task_id), None)
        sprint = next((s for s in sprints if s.get("sprint_id") == sprint_id), None)

        if not task:
            return json.dumps({"error": f"Task '{task_id}' not found"})
        if not sprint:
            return json.dumps({"error": f"Sprint '{sprint_id}' not found"})

        if sprint.get("status") not in ["planning", "active"]:
            return json.dumps(
                {
                    "error": f"Cannot add tasks to sprint in '{sprint.get('status')}' status"
                }
            )

        if sprint.get("status") == "active" and task.get("priority") != "critical":
            return json.dumps(
                {
                    "error": "Cannot add non-critical tasks to active sprint",
                }
            )

        team = next(
            (t for t in teams if t.get("team_id") == sprint.get("team_id")), None
        )
        if team:

            team_members = team.get("members", [])

            completed_sprints = [
                s
                for s in sprints
                if s.get("team_id") == team.get("team_id")
                and s.get("status") == "completed"
            ]

            if len(completed_sprints) >= 3:

                recent_sprints = sorted(
                    completed_sprints, key=lambda x: x.get("end_date", ""), reverse=True
                )[:3]
                avg_velocity = sum(s.get("velocity", 0) for s in recent_sprints) / 3
                capacity_limit = avg_velocity * 0.8
            else:

                capacity_limit = len(team_members) * 20

            sprint_tasks = [t for t in tasks if t.get("sprint_id") == sprint_id]
            current_points = sum(t.get("story_points", 0) for t in sprint_tasks)
            new_total = current_points + task.get("story_points", 0)

            if new_total > capacity_limit:
                return json.dumps(
                    {
                        "error": "Adding task would exceed sprint capacity limit",
                        "current_points": current_points,
                        "task_points": task.get("story_points", 0),
                        "total_would_be": new_total,
                        "capacity_limit": capacity_limit,
                    }
                )

            assignee_sprint_tasks = [
                t
                for t in sprint_tasks
                if t.get("assignee_id") == task.get("assignee_id")
            ]
            assignee_points = sum(
                t.get("story_points", 0) for t in assignee_sprint_tasks
            )

            if assignee_points + task.get("story_points", 0) > 25:
                return json.dumps(
                    {
                        "error": f"Cannot assign task. Would exceed 25 story point limit for {task.get('assignee_id')}",
                        "current_points": assignee_points,
                        "task_points": task.get("story_points", 0),
                        "total_would_be": assignee_points + task.get("story_points", 0),
                    }
                )

        task["sprint_id"] = sprint_id
        task["updated_date"] = datetime.datetime.now().isoformat()

        sprint["planned_story_points"] = sprint.get(
            "planned_story_points", 0
        ) + task.get("story_points", 0)

        return json.dumps(
            {
                "success": True,
                "task": task,
                "sprint_planned_points": sprint["planned_story_points"],
            }
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "assign_task_to_sprint",
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
