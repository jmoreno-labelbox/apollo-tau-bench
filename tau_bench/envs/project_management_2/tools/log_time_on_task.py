from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime
from typing import Any

class LogTimeOnTask(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], task_id: str = None, hours_logged: float = None, employee_id: str = None, notes: str = "") -> str:
        tasks = data.get("tasks", [])
        time_logs = data.get("time_logs", [])

        task = next((t for t in tasks if t.get("task_id") == task_id), None)
        if not task:
            payload = {"error": f"Task '{task_id}' not found"}
            out = json.dumps(payload)
            return out

        if task.get("assignee_id") != employee_id:
            payload = {"error": f"Employee '{employee_id}' is not assigned to this task"}
            out = json.dumps(payload)
            return out

        log_entry = {
            "log_id": f"time_{uuid.uuid4().hex[:8]}",
            "task_id": task_id,
            "employee_id": employee_id,
            "hours": hours_logged,
            "notes": notes,
            "logged_date": datetime.now().isoformat(),
        }
        time_logs.append(log_entry)

        task["time_logged"] = task.get("time_logged", 0) + hours_logged
        task["updated_date"] = datetime.now().isoformat()
        task["last_time_logged"] = datetime.now().isoformat()
        payload = {
            "success": True,
            "time_log": log_entry,
            # "total_time_logged": task["time_logged"],
        }
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "LogTimeOnTask",
                "description": "Log time spent on a task",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "task_id": {
                            "type": "string",
                            "description": "The task ID to log time for",
                        },
                        "hours_logged": {
                            "type": "number",
                            "description": "Number of hours to log",
                        },
                        "employee_id": {
                            "type": "string",
                            "description": "Employee logging the time",
                        },
                        "notes": {
                            "type": "string",
                            "description": "Optional notes about work done",
                        },
                    },
                    "required": ["task_id", "hours_logged", "employee_id"],
                },
            },
        }
