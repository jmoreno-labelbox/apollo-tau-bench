# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class SearchTasks(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], assignee_id, priority, sprint_id, status, task_id, title) -> str:

        tasks = list(data.get("tasks", {}).values())

        if task_id:
            for task in tasks:
                if task.get("task_id") == task_id:
                    return json.dumps(task, indent=2)
            return json.dumps({"error": f"Task with ID '{task_id}' not found"})

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

        return json.dumps(results, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "search_tasks",
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
