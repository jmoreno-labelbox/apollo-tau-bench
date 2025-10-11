# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetSprintFinancialAnalysis(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], sprint_id) -> str:

        if not sprint_id:
            return json.dumps({"error": "sprint_id is required"})

        sprints = data.get("sprints", [])
        tasks = list(data.get("tasks", {}).values())
        task_logs = data.get("task_logs", [])
        employees = list(data.get("employees", {}).values())
        expenses = data.get("expenses", [])

        sprint = next((s for s in sprints if s.get("sprint_id") == sprint_id), None)
        if not sprint:
            return json.dumps({"error": f"Sprint {sprint_id} not found"})

        sprint_tasks = [t for t in tasks if t.get("sprint_id") == sprint_id]

        employee_costs = {}
        total_hours = 0
        total_cost = 0

        for task in sprint_tasks:
            task_time_logs = [
                log for log in task_logs if log.get("task_id") == task["task_id"]
            ]

            for log in task_time_logs:
                employee_id = log.get("employee_id")
                hours = log.get("hours", 0)

                if employee_id not in employee_costs:
                    employee = next(
                        (e for e in employees if e.get("employee_id") == employee_id),
                        None,
                    )
                    if employee:
                        hourly_rate = (
                            150 if "senior" in employee.get("role", "").lower() else 100
                        )
                        employee_costs[employee_id] = {
                            "name": employee["name"],
                            "role": employee["role"],
                            "hours": 0,
                            "hourly_rate": hourly_rate,
                            "cost": 0,
                        }

                if employee_id in employee_costs:
                    employee_costs[employee_id]["hours"] += hours
                    employee_costs[employee_id]["cost"] += (
                        hours * employee_costs[employee_id]["hourly_rate"]
                    )
                    total_hours += hours
                    total_cost += hours * employee_costs[employee_id]["hourly_rate"]

        from datetime import timezone

        sprint_start = datetime.fromisoformat(
            sprint["start_date"].replace("Z", "+00:00")
        )
        sprint_end = datetime.fromisoformat(sprint["end_date"].replace("Z", "+00:00"))

        sprint_expenses = []
        for expense in expenses:
            if expense.get("sprint_id") == sprint_id:
                sprint_expenses.append(expense)
            elif expense.get("submitted_date"):

                try:
                    submitted_date_str = expense["submitted_date"]

                    if submitted_date_str.endswith("Z"):
                        submitted_date = datetime.fromisoformat(
                            submitted_date_str.replace("Z", "+00:00")
                        )
                    elif "+" in submitted_date_str or submitted_date_str.endswith(
                        "+00:00"
                    ):
                        submitted_date = datetime.fromisoformat(submitted_date_str)
                    else:

                        submitted_date = datetime.fromisoformat(
                            submitted_date_str
                        ).replace(tzinfo=timezone.utc)

                    if sprint_start <= submitted_date <= sprint_end:
                        sprint_expenses.append(expense)
                except Exception as e:

                    pass

        total_expenses = sum(
            e.get("amount", 0) for e in sprint_expenses if e.get("status") == "approved"
        )

        planned_points = sprint.get("planned_story_points", 0)
        completed_points = sprint.get("completed_story_points", 0)

        analysis = {
            "sprint_id": sprint_id,
            "sprint_name": sprint["sprint_name"],
            "sprint_status": sprint["status"],
            "financial_summary": {
                "total_personnel_cost": total_cost,
                "total_expense_cost": total_expenses,
                "total_cost": total_cost + total_expenses,
                "total_hours": total_hours,
                "average_hourly_cost": round(total_cost / total_hours, 2)
                if total_hours > 0
                else 0,
            },
            "productivity_metrics": {
                "planned_story_points": planned_points,
                "completed_story_points": completed_points,
                "cost_per_planned_point": round(
                    (total_cost + total_expenses) / planned_points, 2
                )
                if planned_points > 0
                else 0,
                "cost_per_completed_point": round(
                    (total_cost + total_expenses) / completed_points, 2
                )
                if completed_points > 0
                else 0,
                "velocity": sprint.get("velocity", 0),
            },
            "team_costs": {
                "team_members": len(employee_costs),
                "member_breakdown": list(employee_costs.values()),
            },
            "expense_summary": {
                "expense_count": len(sprint_expenses),
                "total_amount": total_expenses,
                "categories": {},
            },
        }

        for expense in sprint_expenses:
            category = expense.get("category", "Other")
            if category not in analysis["expense_summary"]["categories"]:
                analysis["expense_summary"]["categories"][category] = 0
            analysis["expense_summary"]["categories"][category] += expense.get(
                "amount", 0
            )

        return json.dumps(analysis, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_sprint_financial_analysis",
                "description": "Get comprehensive financial analysis for a sprint",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "sprint_id": {"type": "string", "description": "Sprint ID"}
                    },
                    "required": ["sprint_id"],
                },
            },
        }
