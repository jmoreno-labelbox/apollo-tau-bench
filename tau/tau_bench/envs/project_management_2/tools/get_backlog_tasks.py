# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetBacklogTasks(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], max_story_points, priority) -> str:

        tasks = list(data.get("tasks", {}).values())

        backlog_tasks = [
            t for t in tasks if not t.get("sprint_id") and t.get("status") != "done"
        ]

        if priority:
            backlog_tasks = [t for t in backlog_tasks if t.get("priority") == priority]

        if max_story_points := max_story_points:
            backlog_tasks = [
                t for t in backlog_tasks if t.get("story_points", 0) <= max_story_points
            ]

        priority_order = {"critical": 0, "high": 1, "medium": 2, "low": 3}
        backlog_tasks.sort(
            key=lambda x: (
                priority_order.get(x.get("priority", "medium"), 2),
                x.get("story_points", 0),
            )
        )

        return json.dumps(
            {
                "backlog_size": len(backlog_tasks),
                "total_story_points": sum(
                    t.get("story_points", 0) for t in backlog_tasks
                ),
                "tasks": backlog_tasks,
            },
            indent=2,
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_backlog_tasks",
                "description": "Get tasks in the backlog (not assigned to any sprint)",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "priority": {
                            "type": "string",
                            "description": "Filter by priority: low, medium, high, critical",
                        },
                        "max_story_points": {
                            "type": "integer",
                            "description": "Maximum story points to filter by",
                        },
                    },
                },
            },
        }
