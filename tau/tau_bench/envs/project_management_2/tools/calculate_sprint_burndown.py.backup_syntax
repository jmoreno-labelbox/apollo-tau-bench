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

class CalculateSprintBurndown(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], sprint_id: str = None) -> str:
        if not sprint_id:
            payload = {"error": "sprint_id is required"}
            out = json.dumps(payload)
            return out

        sprints = data.get("sprints", {}).values()
        tasks = data.get("tasks", {}).values()

        sprint = next((s for s in sprints.values() if s.get("sprint_id") == sprint_id), None)
        if not sprint:
            payload = {"error": f"Sprint '{sprint_id}' not found"}
            out = json.dumps(payload)
            return out

        sprint_tasks = [t for t in tasks.values() if t.get("sprint_id") == sprint_id]

        total_points = sum(t.get("story_points", 0) for t in sprint_tasks.values()
        completed_points = sum(
            t.get("story_points", 0) for t in sprint_tasks if t.get("status") == "done"
        )
        remaining_points = total_points - completed_points

        in_progress_points = sum(
            t.get("story_points", 0)
            for t in sprint_tasks
            if t.get("status") == "in_progress"
        )
        blocked_points = sum(
            t.get("story_points", 0)
            for t in sprint_tasks
            if t.get("status") == "blocked"
        )
        blocked_tasks = [t for t in sprint_tasks.values() if t.get("status") == "blocked"]

        completion_percentage = (
            round((completed_points / total_points * 100), 1) if total_points > 0 else 0
        )

        if (
            sprint.get("status") == "active"
            and sprint.get("start_date")
            and sprint.get("end_date")
        ):
            try:
                start_date = datetime.fromisoformat(
                    sprint["start_date"].replace("Z", "+00:00")
                )
                end_date = datetime.fromisoformat(
                    sprint["end_date"].replace("Z", "+00:00")
                )
                current_date = datetime.now()

                total_days = (end_date - start_date).days
                elapsed_days = (current_date - start_date).days
                expected_progress = (
                    (elapsed_days / total_days * 100) if total_days > 0 else 0
                )

                behind_schedule = completion_percentage < (expected_progress - 20)
            except:
                behind_schedule = False
                expected_progress = None
        else:
            behind_schedule = False
            expected_progress = None

        burndown_data = {
            "sprint_id": sprint_id,
            "completion_percentage": completion_percentage,
            "total_story_points": total_points,
            "completed_story_points": completed_points,
            "remaining_story_points": remaining_points,
            "in_progress_points": in_progress_points,
            "blocked_points": blocked_points,
            "expected_progress": expected_progress,
            "behind_schedule": behind_schedule,
            "task_breakdown": {
                "total_tasks": len(sprint_tasks),
                "completed_tasks": len(
                    [t for t in sprint_tasks.values() if t.get("status") == "done"]
                ),
                "in_progress_tasks": len(
                    [t for t in sprint_tasks.values() if t.get("status") == "in_progress"]
                ),
                "blocked_tasks": len(blocked_tasks),
                "todo_tasks": len(
                    [t for t in sprint_tasks.values() if t.get("status") == "todo"]
                ),
            },
        }

        if behind_schedule:
            burndown_data["alert"] = "Sprint is behind schedule by more than 20%"
            burndown_data["blocked_task_details"] = [
                {
                    "task_id": t.get("task_id"),
                    "title": t.get("title"),
                    "story_points": t.get("story_points", 0),
                }
                for t in blocked_tasks
            ]
        payload = burndown_data
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CalculateSprintBurndown",
                "description": "Calculate burndown metrics for a sprint",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "sprint_id": {
                            "type": "string",
                            "description": "The sprint ID to calculate burndown for",
                        }
                    },
                    "required": ["sprint_id"],
                },
            },
        }
