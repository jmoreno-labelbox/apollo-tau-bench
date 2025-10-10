# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CheckBlockedTasksForEscalation(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        check_all_sprints = kwargs.get("check_all_sprints", True)

        tasks = list(data.get("tasks", {}).values())
        task_history = list(data.get("task_history", {}).values())

        if sprint_id := kwargs.get("sprint_id"):
            tasks_to_check = [t for t in tasks if t.get("sprint_id") == sprint_id]
        elif check_all_sprints:
            tasks_to_check = tasks
        else:
            return json.dumps(
                {
                    "error": "Either check_all_sprints must be True or sprint_id must be provided"
                }
            )

        blocked_tasks = [t for t in tasks_to_check if t.get("status") == "blocked"]

        tasks_needing_escalation = []

        for task in blocked_tasks:

            if task.get("escalated", False):
                continue

            task_id = task.get("task_id")
            blocked_history = [
                h
                for h in task_history
                if h.get("task_id") == task_id
                and h.get("action") == "status_changed"
                and h.get("to_status") == "blocked"
            ]

            days_blocked = "2+"
            if blocked_history:
                blocked_history.sort(key=lambda x: x.get("timestamp", ""), reverse=True)

                days_blocked = "365+"

            tasks_needing_escalation.append(
                {
                    "task_id": task.get("task_id"),
                    "title": task.get("title"),
                    "assignee_id": task.get("assignee_id"),
                    "days_blocked": days_blocked,
                    "current_priority": task.get("priority"),
                }
            )

        return json.dumps(
            {
                "total_blocked_tasks": len(blocked_tasks),
                "tasks_needing_escalation": len(tasks_needing_escalation),
                "tasks": tasks_needing_escalation,
            },
            indent=2,
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "check_blocked_tasks_for_escalation",
                "description": "Check for blocked tasks that need escalation (blocked > 2 days)",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "check_all_sprints": {
                            "type": "boolean",
                            "description": "Check all sprints (default: True)",
                        },
                        "sprint_id": {
                            "type": "string",
                            "description": "Specific sprint to check",
                        },
                    },
                },
            },
        }
