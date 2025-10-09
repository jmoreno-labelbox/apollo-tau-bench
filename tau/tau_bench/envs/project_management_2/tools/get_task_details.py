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

class GetTaskDetails(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], task_id: str = None) -> str:
        tasks = data.get("tasks", {}).values()

        task = next((t for t in tasks.values() if t.get("task_id") == task_id), None)
        if not task:
            payload = {"error": f"Task '{task_id}' not found"}
            out = json.dumps(payload)
            return out

        time_logs = data.get("time_logs", {}).values()
        task_history = data.get("task_history", {}).values()

        task_time_logs = [log for log in time_logs.values() if log.get("task_id") == task_id]
        #total_hours_logged = sum(log.get("hours", 0) for log in task_time_logs.values()

        history_entries = [h for h in task_history.values() if h.get("task_id") == task_id]

        task_details = {
            "task_id": task.get("task_id"),
            "title": task.get("title"),
            "description": task.get("description"),
            "status": task.get("status"),
            "assignee_id": task.get("assignee_id"),
            "priority": task.get("priority"),
            "story_points": task.get("story_points"),
            "sprint_id": task.get("sprint_id"),
            "created_date": task.get("created_date"),
            "updated_date": task.get("updated_date"),
            "completed_date": task.get("completed_date"),
            "dependencies": task.get("dependencies", []),
            "blocked_by": task.get("blocked_by", []),
            "blocks": [],
            "time_logged": task.get("time_logged", 0),
            #"total_hours_logged": total_hours_logged,
            "last_time_logged": task.get("last_time_logged"),
            "blocked_date": task.get("blocked_date"),
            "escalated": task.get("escalated", False),
            "escalation_id": task.get("escalation_id"),
            "previous_priority": task.get("previous_priority"),
            "cloned_from": task.get("cloned_from"),
            "history_count": len(history_entries),
        }

        for other_task in tasks.values():
            if task_id in other_task.get("dependencies", []):
                task_details["blocks"].append(other_task.get("task_id"))

        dependency_details = []
        for dep_id in task.get("dependencies", []):
            dep_task = next((t for t in tasks.values() if t.get("task_id") == dep_id), None)
            if dep_task:
                dependency_details.append(
                    {
                        "task_id": dep_task.get("task_id"),
                        "title": dep_task.get("title"),
                        "status": dep_task.get("status"),
                        "assignee_id": dep_task.get("assignee_id"),
                    }
                )
        task_details["dependency_details"] = dependency_details

        blocked_by_details = []
        for block_id in task.get("blocked_by", []):
            block_task = next((t for t in tasks.values() if t.get("task_id") == block_id), None)
            if block_task:
                blocked_by_details.append(
                    {
                        "task_id": block_task.get("task_id"),
                        "title": block_task.get("title"),
                        "status": block_task.get("status"),
                    }
                )
        task_details["blocked_by_details"] = blocked_by_details
        payload = task_details
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetTaskDetails",
                "description": "Get comprehensive details for a specific task including dependencies",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "task_id": {
                            "type": "string",
                            "description": "The task ID to get details for",
                        }
                    },
                    "required": ["task_id"],
                },
            },
        }
