# Copyright Sierra

import datetime, uuid
import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ResolveBlockedTask(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], resolution, task_id, unblock_dependencies = False) -> str:

        if not all([task_id, resolution]):
            return json.dumps({"error": "task_id and resolution are required"})

        tasks = list(data.get("tasks", {}).values())
        task_history = list(data.get("task_history", {}).values())

        task = next((t for t in tasks if t.get("task_id") == task_id), None)
        if not task:
            return json.dumps({"error": f"Task '{task_id}' not found"})

        # if task["status"] != "blocked":
        # return json.dumps({"error": "Task is not in a blocked state"})

        unresolved_deps = []

        if unblock_dependencies:
            task["blocked_by"] = []
        else:
            for dep_id in task.get("dependencies", []):
                dep_task = next((t for t in tasks if t.get("task_id") == dep_id), None)

                if dep_task and dep_task.get("status") != "done":
                    unresolved_deps.append(dep_id)

        if unresolved_deps:
            return json.dumps(
                {
                    "error": "Cannot unblock task - dependencies not resolved",
                    "unresolved_dependencies": unresolved_deps,
                }
            )

        history_entry = {
            "history_id": f"hist_{uuid.uuid4().hex[:8]}",
            "task_id": task_id,
            "action": "unblocked",
            "resolution": resolution,
            "timestamp": datetime.now().isoformat(),
        }
        task_history.append(history_entry)

        task["status"] = "todo"
        task["blocked_date"] = None
        task["updated_date"] = datetime.now().isoformat()

        if task.get("escalated"):
            escalations = list(data.get("escalations", {}).values())
            for esc in escalations:
                if esc.get("task_id") == task_id and not esc.get("resolved"):
                    esc["resolved"] = True
                    esc["resolution_date"] = datetime.now().isoformat()
                    esc["resolution"] = resolution

        return json.dumps({"success": True, "task": task, "resolution": resolution})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "resolve_blocked_task",
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
