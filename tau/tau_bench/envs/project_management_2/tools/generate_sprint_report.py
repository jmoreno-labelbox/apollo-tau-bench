# Copyright Sierra

import datetime
import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GenerateSprintReport(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], sprint_id) -> str:

        if not sprint_id:
            return json.dumps({"error": "sprint_id is required"})

        sprints = list(data.get("sprints", {}).values())
        tasks = list(data.get("tasks", {}).values())
        time_logs = list(data.get("time_logs", {}).values())

        sprint = next((s for s in sprints if s.get("sprint_id") == sprint_id), None)
        if not sprint:
            return json.dumps({"error": f"Sprint '{sprint_id}' not found"})

        sprint_tasks = [t for t in tasks if t.get("sprint_id") == sprint_id]

        total_tasks = len(sprint_tasks)
        completed_tasks = [t for t in sprint_tasks if t.get("status") == "done"]
        blocked_tasks = [t for t in sprint_tasks if t.get("status") == "blocked"]

        sprint_time_logs = [
            log
            for log in time_logs
            if any(t.get("task_id") == log.get("task_id") for t in sprint_tasks)
        ]
        # total_hours_logged = sum(log.get("hours", 0) for log in sprint_time_logs)

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
                    logged_hours = sum(log.get("hours", 0) for log in task_logs)
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
                # "total_hours_recorded": total_hours_logged,
                "total_tasks": total_tasks,
                "completed_tasks": len(completed_tasks),
                "blocked_tasks": len(blocked_tasks),
                "completion_percentage": round(
                    (len(completed_tasks) / total_tasks * 100), 1
                )
                if total_tasks > 0
                else 0,
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
            "report_generated": datetime.datetime.now().isoformat(),
        }

        return json.dumps(report, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "generate_sprint_report",
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
