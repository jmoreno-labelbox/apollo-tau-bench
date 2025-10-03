from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime
from typing import Any

class BulkMoveTasksToSprint(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], task_ids: list = None, target_sprint_id: str = None) -> str:
        if task_ids is None:
            task_ids = []

        if not all([task_ids, target_sprint_id]):
            payload = {"error": "task_ids and target_sprint_id are required"}
            out = json.dumps(payload)
            return out

        tasks = data.get("tasks", [])
        sprints = data.get("sprints", [])
        teams = data.get("teams", [])

        sprint = next(
            (s for s in sprints if s.get("sprint_id") == target_sprint_id), None
        )
        if not sprint:
            payload = {"error": f"Sprint '{target_sprint_id}' not found"}
            out = json.dumps(payload)
            return out

        if sprint.get("status") not in ["planning", "active"]:
            payload = {
                    "error": f"Cannot add tasks to sprint in '{sprint.get('status')}' status"
                }
            out = json.dumps(
                payload)
            return out

        team = next(
            (t for t in teams if t.get("team_id") == sprint.get("team_id")), None
        )
        if not team:
            payload = {"error": "Sprint team not found"}
            out = json.dumps(payload)
            return out

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

        sprint_tasks = [t for t in tasks if t.get("sprint_id") == target_sprint_id]
        current_points = sum(t.get("story_points", 0) for t in sprint_tasks)

        moved_tasks = []
        failed_tasks = []
        total_points_to_add = 0
        assignee_workloads = {}

        for member_id in team_members:
            member_tasks = [
                t for t in sprint_tasks if t.get("assignee_id") == member_id
            ]
            assignee_workloads[member_id] = sum(
                t.get("story_points", 0) for t in member_tasks
            )

        for task_id in task_ids:
            task = next((t for t in tasks if t.get("task_id") == task_id), None)
            if not task:
                failed_tasks.append({"task_id": task_id, "reason": "Task not found"})
                continue

            if task.get("status") == "done":
                failed_tasks.append(
                    {"task_id": task_id, "reason": "Cannot move completed tasks"}
                )
                continue

            if sprint.get("status") == "active" and task.get("priority") != "critical":
                failed_tasks.append(
                    {
                        "task_id": task_id,
                        "reason": "Only critical tasks can be added to active sprints",
                    }
                )
                continue

            task_points = task.get("story_points", 0)

            if current_points + total_points_to_add + task_points > capacity_limit:
                failed_tasks.append(
                    {
                        "task_id": task_id,
                        "reason": f"Would exceed sprint capacity ({capacity_limit} points)",
                    }
                )
                continue

            assignee_id = task.get("assignee_id")
            if assignee_id in assignee_workloads:
                if assignee_workloads[assignee_id] + task_points > 25:
                    failed_tasks.append(
                        {
                            "task_id": task_id,
                            "reason": f"Would exceed 25 point limit for {assignee_id}",
                        }
                    )
                    continue

            old_sprint = task.get("sprint_id")
            total_points_to_add += task_points
            if assignee_id in assignee_workloads:
                assignee_workloads[assignee_id] += task_points

            moved_tasks.append(
                {
                    "task_id": task_id,
                    "from_sprint": old_sprint,
                    "story_points": task_points,
                }
            )

            task["sprint_id"] = target_sprint_id
            task["updated_date"] = datetime.now().isoformat()

        sprint["planned_story_points"] = current_points + total_points_to_add
        payload = {
                "success": True,
                "moved_count": len(moved_tasks),
                "failed_count": len(failed_tasks),
                "total_points_added": total_points_to_add,
                "moved_tasks": moved_tasks,
                "failed_tasks": failed_tasks,
                "sprint_total_points": sprint["planned_story_points"],
            }
        out = json.dumps(
            payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "BulkMoveTasksToSprint",
                "description": "Move multiple tasks to a sprint at once",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "task_ids": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of task IDs to move",
                        },
                        "target_sprint_id": {
                            "type": "string",
                            "description": "Target sprint ID",
                        },
                    },
                    "required": ["task_ids", "target_sprint_id"],
                },
            },
        }
