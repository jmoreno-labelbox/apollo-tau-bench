# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateTaskDependency(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        task_id = kwargs.get("task_id")
        depends_on_task_id = kwargs.get("depends_on_task_id")
        block_task = kwargs.get("block_task")

        if not all([task_id, depends_on_task_id]):
            return json.dumps({"error": "task_id and depends_on_task_id are required"})

        if task_id == depends_on_task_id:
            return json.dumps({"error": "Task cannot depend on itself"})

        tasks = list(data.get("tasks", {}).values())

        task = next((t for t in tasks if t.get("task_id") == task_id), None)
        dependency_task = next(
            (t for t in tasks if t.get("task_id") == depends_on_task_id), None
        )

        if not task:
            return json.dumps({"error": f"Task '{task_id}' not found"})
        if not dependency_task:
            return json.dumps(
                {"error": f"Dependency task '{depends_on_task_id}' not found"}
            )

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
            return json.dumps(
                {"error": "Creating this dependency would create a circular dependency"}
            )

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

        return json.dumps({"success": True, "task": task})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_task_dependency",
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
