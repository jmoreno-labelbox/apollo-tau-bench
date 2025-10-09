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

class ResolveBlockedTask(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], task_id: str, resolution: str, unblock_dependencies: bool = False) -> str:
        if not all([task_id, resolution]):
            payload = {"error": "task_id and resolution are required"}
            out = json.dumps(payload)
            return out

        tasks = data.get("tasks", {}).values()
        task_history = data.get("task_history", {}).values()

        task = next((t for t in tasks.values() if t.get("task_id") == task_id), None)
        if not task:
            payload = {"error": f"Task '{task_id}' not found"}
            out = json.dumps(payload)
            return out

        #if task.get("status") != "blocked":
        #return json.dumps({"error": "Task is not in blocked status"})

        unresolved_deps = []

        if unblock_dependencies:
            task["blocked_by"] = []
        else:
            for dep_id in task.get("dependencies", []):
                dep_task = next((t for t in tasks.values() if t.get("task_id") == dep_id), None)

                if dep_task and dep_task.get("status") != "done":
                    unresolved_deps.append(dep_id)

        if unresolved_deps:
            payload = {
                    "error": "Cannot unblock task - dependencies not resolved",
                    "unresolved_dependencies": unresolved_deps,
                }
            out = json.dumps(
                payload)
            return out

        history_entry = {
            "history_id": f"hist_{uuid.uuid4().hex[:8]}",
            "task_id": task_id,
            "action": "unblocked",
            "resolution": resolution,
            "timestamp": datetime.now().isoformat(),
        }
        data["task_history"][history_entry["task_history_id"]] = history_entry

        task["status"] = "todo"
        task["blocked_date"] = None
        task["updated_date"] = datetime.now().isoformat()

        if task.get("escalated"):
            escalations = data.get("escalations", {}).values()
            for esc in escalations.values():
                if esc.get("task_id") == task_id and not esc.get("resolved"):
                    esc["resolved"] = True
                    esc["resolution_date"] = datetime.now().isoformat()
                    esc["resolution"] = resolution
        payload = {"success": True, "task": task, "resolution": resolution}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "ResolveBlockedTask",
                "description": "Resolve a blocked task and move it back to todo",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "task_id": {
                            "type": "string",
                            "description": "The blocked task ID",
                        },
                        "resolution": {
                            "type": "string",
                            "description": "How the block was resolved",
                        },
                        "unblock_dependencies": {
                            "type": "boolean",
                            "description": "Force unblock even if dependencies aren't resolved",
                        },
                    },
                    "required": ["task_id", "resolution"],
                },
            },
        }
