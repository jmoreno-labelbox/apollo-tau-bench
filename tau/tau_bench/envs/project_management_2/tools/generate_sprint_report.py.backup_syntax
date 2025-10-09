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

class GenerateSprintReport(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], sprint_id: str = None) -> str:
        if not sprint_id:
            payload = {"error": "sprint_id is required"}
            out = json.dumps(payload)
            return out

        sprints = data.get("sprints", {}).values()
        tasks = data.get("tasks", {}).values()
        time_logs = data.get("time_logs", {}).values()

        sprint = next((s for s in sprints.values() if s.get("sprint_id") == sprint_id), None)
        if not sprint:
            payload = {"error": f"Sprint '{sprint_id}' not found"}
            out = json.dumps(payload)
            return out

        sprint_tasks = [t for t in tasks.values() if t.get("sprint_id") == sprint_id]

        total_tasks = len(sprint_tasks)
        completed_tasks = [t for t in sprint_tasks.values() if t.get("status") == "done"]
        blocked_tasks = [t for t in sprint_tasks.values() if t.get("status") == "blocked"]

        sprint_time_logs = [
            log
            for log in time_logs.values() if any(t.get("task_id") == log.get("task_id") for t in sprint_tasks.values()
        ]
        #total_hours_logged = sum(log.get("hours", 0) for log in sprint_time_logs.values()

        assignee_performance = {}
        for task in sprint_tasks:
            assignee = task.get("assignee_id")
            if assignee not in assignee_performance:
                assignee_performance[assignee] = {
                    "completed_points": 0,
                    "total_points": 0,
                    "completed_tasks": 0,
                    "total_tasks": 0,
                }

            assignee_performance[assignee]["total_tasks"] += 1
            assignee_performance[assignee]["total_points"] += task.get(
                "story_points", 0
            )

            if task.get("status") == "done":
                assignee_performance[assignee]["completed_tasks"] += 1
                assignee_performance[assignee]["completed_points"] += task.get(
                    "story_points", 0
                )

        compliance_issues = []

        for task in sprint_tasks:
            if task.get("status") in ["in_progress", "done"]:
                task_logs = [
                    log
                    for log in sprint_time_logs
                    if log.get("task_id") == task.get("task_id")
                ]
                if task.get("status") == "done":
                    required_hours = task.get("story_points", 0) * 2 * 0.5
                    logged_hours = sum(log.get("hours", 0) for log in task_logs.values()
                    if logged_hours < required_hours:
                        compliance_issues.append(
                            {
                                "type": "insufficient_time_logged",
                                "task_id": task.get("task_id"),
                                "required_hours": required_hours,
                                "logged_hours": logged_hours,
                            }
                        )

        risks = []
        if len(blocked_tasks) > total_tasks * 0.2:
            risks.append("High number of blocked tasks (>20%)")
        if (
            sprint.get("status") == "active"
            and sprint.get("completed_story_points", 0)
            < sprint.get("planned_story_points", 0) * 0.3
        ):
            risks.append("Low completion rate for active sprint")

        report = {
            "compliance_issues": compliance_issues,
            "sprint_id": sprint_id,
            "sprint_name": sprint.get("sprint_name"),
            "status": sprint.get("status"),
            "metrics": {
                "planned_story_points": sprint.get("planned_story_points", 0),
                #"total_hours_logged": total_hours_logged,
                "total_tasks": total_tasks,
                "completed_tasks": len(completed_tasks),
                "blocked_tasks": len(blocked_tasks),
                "completion_percentage": (
                    round((len(completed_tasks) / total_tasks * 100), 1)
                    if total_tasks > 0
                    else 0
                ),
                "completed_story_points": sprint.get("completed_story_points", 0),
                "velocity": sprint.get("velocity", 0),
            },
            "team_performance": assignee_performance,
            "blocked_task_details": [
                {
                    "task_id": t.get("task_id"),
                    "title": t.get("title"),
                    "assignee": t.get("assignee_id"),
                }
                for t in blocked_tasks
            ],
            "risks": risks,
            "report_generated": datetime.now().isoformat(),
        }
        payload = report
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GenerateSprintReport",
                "description": "Generate a comprehensive report for a sprint",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "sprint_id": {
                            "type": "string",
                            "description": "The sprint ID to generate report for",
                        }
                    },
                    "required": ["sprint_id"],
                },
            },
        }
