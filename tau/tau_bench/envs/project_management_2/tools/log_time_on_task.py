# Sierra Copyright

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class LogTimeOnTask(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        task_id = kwargs.get("task_id")
        hours_logged = kwargs.get("hours_logged")
        employee_id = kwargs.get("employee_id")
        notes = kwargs.get("notes", "")

        tasks = list(data.get("tasks", {}).values())
        time_logs = list(data.get("time_logs", {}).values())

        task = next((t for t in tasks if t.get("task_id") == task_id), None)
        if not task:
            return json.dumps({"error": f"Task '{task_id}' not found"})

        if task.get("assignee_id") != employee_id:
            return json.dumps(
                {"error": f"Employee '{employee_id}' is not assigned to this task"}
            )

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

        return json.dumps(
            {
                "success": True,
                "time_log": log_entry,
                # "total_time_recorded": task["time_logged"],
            }
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "log_time_on_task",
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
