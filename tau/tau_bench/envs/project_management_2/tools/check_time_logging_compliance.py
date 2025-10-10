# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CheckTimeLoggingCompliance(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        sprint_id = kwargs.get("sprint_id")
        check_all = kwargs.get("check_all", False)

        tasks = list(data.get("tasks", {}).values())
        time_logs = list(data.get("time_logs", {}).values())

        if sprint_id:
            tasks_to_check = [t for t in tasks if t.get("sprint_id") == sprint_id]
        elif check_all:
            tasks_to_check = tasks
        else:
            return json.dumps(
                {"error": "Either sprint_id must be provided or check_all must be True"}
            )

        non_compliant_tasks = []

        for task in tasks_to_check:
            if task.get("status") in ["in_progress", "done"]:

                last_logged = task.get("last_time_logged")
                if last_logged:
                    try:
                        last_logged_date = datetime.fromisoformat(
                            last_logged.replace("Z", "+00:00")
                        )
                        days_since_logged = (datetime.now() - last_logged_date).days

                        if days_since_logged > 2:
                            non_compliant_tasks.append(
                                {
                                    "task_id": task.get("task_id"),
                                    "title": task.get("title"),
                                    "assignee_id": task.get("assignee_id"),
                                    "status": task.get("status"),
                                    "days_since_logged": days_since_logged,
                                    "issue": "No time logged in over 2 days",
                                }
                            )
                    except:
                        pass
                else:

                    non_compliant_tasks.append(
                        {
                            "task_id": task.get("task_id"),
                            "title": task.get("title"),
                            "assignee_id": task.get("assignee_id"),
                            "status": task.get("status"),
                            "issue": "No time ever logged",
                        }
                    )

                if task.get("status") == "done":
                    task_logs = [
                        log
                        for log in time_logs
                        if log.get("task_id") == task.get("task_id")
                    ]
                    total_hours = sum(log.get("hours", 0) for log in task_logs)
                    required_hours = task.get("story_points", 0) * 2 * 0.5

                    if total_hours < required_hours:
                        existing = next(
                            (
                                t
                                for t in non_compliant_tasks
                                if t["task_id"] == task["task_id"]
                            ),
                            None,
                        )
                        if existing:
                            existing["insufficient_hours"] = {
                                "logged": total_hours,
                                "required": required_hours,
                            }
                        else:
                            non_compliant_tasks.append(
                                {
                                    "task_id": task.get("task_id"),
                                    "title": task.get("title"),
                                    "assignee_id": task.get("assignee_id"),
                                    "status": "done",
                                    "issue": "Insufficient hours logged",
                                    "insufficient_hours": {
                                        "logged": total_hours,
                                        "required": required_hours,
                                    },
                                }
                            )

        return json.dumps(
            {
                "tasks_checked": len(tasks_to_check),
                "non_compliant_count": len(non_compliant_tasks),
                "non_compliant_tasks": non_compliant_tasks,
            },
            indent=2,
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "check_time_logging_compliance",
                "description": "Check time logging compliance for tasks",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "sprint_id": {
                            "type": "string",
                            "description": "Sprint ID to check",
                        },
                        "check_all": {
                            "type": "boolean",
                            "description": "Check all tasks regardless of sprint",
                        },
                    },
                },
            },
        }
