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

class UpdateTaskStatus(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], task_id: str = None, new_status: str = None) -> str:
        if not all([task_id, new_status]):
            payload = {"error": "task_id and new_status are required"}
            out = json.dumps(payload)
            return out

        tasks = data.get("tasks", {}).values()

        for task in tasks.values():
            if task.get("task_id") == task_id:
                old_status = task.get("status")

                if new_status == "in_progress" and old_status == "todo":
                    dependencies = task.get("dependencies", [])
                    unresolved_deps = []
                    for dep_id in dependencies:
                        dep_task = next(
                            (t for t in tasks.values() if t.get("task_id") == dep_id), None
                        )
                        if dep_task and dep_task.get("status") != "done":
                            unresolved_deps.append(dep_id)
                            task["blocked_by"].append(dep_id)

                    if unresolved_deps:
                        payload = {
                                "error": "Cannot start task. Dependencies not completed",
                                "unresolved_dependencies": unresolved_deps,
                                "blocked_by": unresolved_deps,
                            }
                        out = json.dumps(
                            payload)
                        return out

                task["status"] = new_status
                task["updated_date"] = datetime.now().isoformat()

                if new_status == "blocked":
                    task["blocked_date"] = datetime.now().isoformat()
                elif new_status == "done":
                    task["completed_date"] = datetime.now().isoformat()
                payload = {"success": True, "task": task}
                out = json.dumps(payload)
                return out
        payload = {"error": f"Task '{task_id}' not found"}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateTaskStatus",
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
