# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CalculateProjectCost(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        project_id = kwargs.get("project_id")
        include_planned = kwargs.get("include_planned", True)
        as_of_date = kwargs.get("as_of_date")

        if not project_id:
            return json.dumps({"error": "project_id is required"})

        allocations = data.get("allocations", [])
        employees = list(data.get("employees", {}).values())
        tasks = list(data.get("tasks", {}).values())
        task_logs = data.get("task_logs", [])
        expenses = data.get("expenses", [])

        project_allocations = [
            a for a in allocations if a.get("project_id") == project_id
        ]

        actual_personnel_cost = 0
        planned_personnel_cost = 0

        for allocation in project_allocations:
            employee = next(
                (
                    e
                    for e in employees
                    if e.get("employee_id") == allocation.get("employee_id")
                ),
                None,
            )
            if employee:

                hourly_rate = (
                    150 if "senior" in employee.get("role", "").lower() else 100
                )
                if "architect" in employee.get("role", "").lower():
                    hourly_rate = 200
                elif "junior" in employee.get("role", "").lower():
                    hourly_rate = 75

                employee_tasks = [
                    t
                    for t in tasks
                    if t.get("assignee_id") == employee["employee_id"]
                    and t.get("sprint_id")
                    and any(a.get("project_id") == project_id for a in allocations)
                ]

                actual_hours = 0
                for task in employee_tasks:
                    task_hours = sum(
                        log.get("hours", 0)
                        for log in task_logs
                        if log.get("task_id") == task["task_id"]
                    )
                    actual_hours += task_hours

                actual_personnel_cost += actual_hours * hourly_rate

                if include_planned:
                    weeks = 26
                    planned_personnel_cost += (
                        allocation.get("hours_per_week", 0) * hourly_rate * weeks
                    )

        project_expenses = [
            e
            for e in expenses
            if e.get("project_id") == project_id and e.get("status") == "approved"
        ]
        non_personnel_cost = sum(e.get("amount", 0) for e in project_expenses)

        teams = data.get("teams", [])
        project_teams = [t for t in teams if t.get("project_id") == project_id]

        cost_breakdown = {
            "project_id": project_id,
            "actual_costs": {
                "personnel": actual_personnel_cost,
                "non_personnel": non_personnel_cost,
                "total": actual_personnel_cost + non_personnel_cost,
            },
            "planned_costs": {
                "personnel": planned_personnel_cost,
                "total": planned_personnel_cost + (planned_personnel_cost * 0.25),
            }
            if include_planned
            else None,
            "cost_per_story_point": 0,
            "team_count": len(project_teams),
            "allocation_count": len(project_allocations),
            "burn_rate_weekly": actual_personnel_cost / 26
            if actual_personnel_cost > 0
            else 0,
        }

        completed_story_points = sum(
            t.get("story_points", 0)
            for t in tasks
            if t.get("status") == "done"
            and any(
                a.get("project_id") == project_id
                for a in allocations
                if a.get("employee_id") == t.get("assignee_id")
            )
        )

        if completed_story_points > 0:
            cost_breakdown["cost_per_story_point"] = round(
                actual_personnel_cost / completed_story_points, 2
            )

        return json.dumps(cost_breakdown, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "calculate_project_cost",
                "description": "Calculate actual and planned costs for a project based on team allocations and logged hours",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "project_id": {"type": "string", "description": "Project ID"},
                        "include_planned": {
                            "type": "boolean",
                            "description": "Include planned costs",
                        },
                        "as_of_date": {
                            "type": "string",
                            "description": "Calculate as of specific date",
                        },
                    },
                    "required": ["project_id"],
                },
            },
        }
