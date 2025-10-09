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

class GetBacklogTasks(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], priority: str = None, max_story_points: int = None) -> str:
        tasks = data.get("tasks", [])

        backlog_tasks = [
            t for t in tasks if not t.get("sprint_id") and t.get("status") != "done"
        ]

        if priority:
            backlog_tasks = [t for t in backlog_tasks if t.get("priority") == priority]

        if max_story_points:
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
        payload = {
            "backlog_size": len(backlog_tasks),
            "total_story_points": sum(
                t.get("story_points", 0) for t in backlog_tasks
            ),
            "tasks": backlog_tasks,
        }
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetBacklogTasks",
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
