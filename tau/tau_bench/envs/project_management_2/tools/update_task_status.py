# Sierra Copyright

import datetime
import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateTaskStatus(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], new_status, task_id) -> str:

        if not all([task_id, new_status]):
            return json.dumps({"error": "task_id and new_status are required"})

        tasks = list(data.get("tasks", {}).values())

        for task in tasks:
            if task.get("task_id") == task_id:
                old_status = task.get("status")

                if new_status == "in_progress" and old_status == "todo":
                    dependencies = task.get("dependencies", [])
                    unresolved_deps = []
                    for dep_id in dependencies:
                        dep_task = next(
                            (t for t in tasks if t.get("task_id") == dep_id), None
                        )
                        if dep_task and dep_task.get("status") != "done":
                            unresolved_deps.append(dep_id)
                            task["blocked_by"].append(dep_id)

                    if unresolved_deps:
                        return json.dumps(
                            {
                                "error": f"Cannot start task. Dependencies not completed",
                                "unresolved_dependencies": unresolved_deps,
                                "blocked_by": unresolved_deps,
                            }
                        )

                task["status"] = new_status
                task["updated_date"] = datetime.datetime.now().isoformat()

                if new_status == "blocked":
                    task["blocked_date"] = datetime.datetime.now().isoformat()
                elif new_status == "done":
                    task["completed_date"] = datetime.datetime.now().isoformat()

                return json.dumps({"success": True, "task": task})

        return json.dumps({"error": f"Task '{task_id}' not found"})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_task_status",
                "description": "Update the status of a task",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "task_id": {
                            "type": "string",
                            "description": "The task ID to update",
                        },
                        "new_status": {
                            "type": "string",
                            "description": "New status: todo, in_progress, blocked, done",
                        },
                    },
                    "required": ["task_id", "new_status"],
                },
            },
        }
