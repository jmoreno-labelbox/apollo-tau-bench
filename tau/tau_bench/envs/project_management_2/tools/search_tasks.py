from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class SearchTasks(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any], 
        task_id: str = None, 
        title: str = None, 
        status: str = None, 
        assignee_id: str = None, 
        sprint_id: str = None, 
        priority: str = None
    ) -> str:
        tasks = data.get("tasks", [])

        if task_id:
            for task in tasks:
                if task.get("task_id") == task_id:
                    payload = task
                    out = json.dumps(payload, indent=2)
                    return out
            payload = {"error": f"Task with ID '{task_id}' not found"}
            out = json.dumps(payload)
            return out

        results = []
        for task in tasks:
            match = True

            if title and title.lower() not in task.get("title", "").lower():
                match = False
            if status and task.get("status") != status:
                match = False
            if assignee_id and task.get("assignee_id") != assignee_id:
                match = False
            if sprint_id and task.get("sprint_id") != sprint_id:
                match = False
            if priority and task.get("priority") != priority:
                match = False

            if match:
                results.append(task)
        payload = results
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SearchTasks",
                "description": "Search for tasks by various criteria",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "task_id": {
                            "type": "string",
                            "description": "Specific task ID to retrieve",
                        },
                        "title": {
                            "type": "string",
                            "description": "Search by task title",
                        },
                        "status": {
                            "type": "string",
                            "description": "Filter by status: todo, in_progress, blocked, done",
                        },
                        "assignee_id": {
                            "type": "string",
                            "description": "Filter by assigned employee ID",
                        },
                        "sprint_id": {
                            "type": "string",
                            "description": "Filter by sprint ID",
                        },
                        "priority": {
                            "type": "string",
                            "description": "Filter by priority: low, medium, high, critical",
                        },
                    },
                },
            },
        }
