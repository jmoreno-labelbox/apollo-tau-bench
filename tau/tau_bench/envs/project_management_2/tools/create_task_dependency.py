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

class CreateTaskDependency(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], task_id: str = None, depends_on_task_id: str = None, block_task: bool = False) -> str:
        if not all([task_id, depends_on_task_id]):
            payload = {"error": "task_id and depends_on_task_id are required"}
            out = json.dumps(payload)
            return out

        if task_id == depends_on_task_id:
            payload = {"error": "Task cannot depend on itself"}
            out = json.dumps(payload)
            return out

        tasks = data.get("tasks", [])

        task = next((t for t in tasks if t.get("task_id") == task_id), None)
        dependency_task = next(
            (t for t in tasks if t.get("task_id") == depends_on_task_id), None
        )

        if not task:
            payload = {"error": f"Task '{task_id}' not found"}
            out = json.dumps(payload)
            return out
        if not dependency_task:
            payload = {"error": f"Dependency task '{depends_on_task_id}' not found"}
            out = json.dumps(payload)
            return out

        def has_circular_dependency(start_id, check_id, visited=None):
            if visited is None:
                visited = set()
            if start_id in visited:
                return True
            visited.add(start_id)

            task_to_check = next(
                (t for t in tasks if t.get("task_id") == start_id), None
            )
            if not task_to_check:
                return False

            for dep_id in task_to_check.get("dependencies", []):
                if dep_id == check_id:
                    return True
                if has_circular_dependency(dep_id, check_id, visited):
                    return True
            return False

        if has_circular_dependency(depends_on_task_id, task_id):
            payload = {"error": "Creating this dependency would create a circular dependency"}
            out = json.dumps(payload)
            return out

        if depends_on_task_id not in task.get("dependencies", []):
            if "dependencies" not in task:
                task["dependencies"] = []
            task["dependencies"].append(depends_on_task_id)
            task["updated_date"] = datetime.now().isoformat()

        if block_task or (
            task.get("status") == "in_progress"
            and dependency_task.get("status") != "done"
        ):
            task["status"] = "todo"
            if "blocked_by" not in task:
                task["blocked_by"] = []
            task["blocked_by"].append(depends_on_task_id)
        payload = {"success": True, "task": task}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateTaskDependency",
                "description": "Create a dependency between two tasks",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "task_id": {
                            "type": "string",
                            "description": "The task that will depend on another",
                        },
                        "depends_on_task_id": {
                            "type": "string",
                            "description": "The task that must be completed first",
                        },
                    },
                    "required": ["task_id", "depends_on_task_id"],
                },
            },
        }
