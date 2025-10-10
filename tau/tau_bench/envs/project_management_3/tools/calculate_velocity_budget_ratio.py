# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CalculateVelocityBudgetRatio(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], team_id, fiscal_year = datetime.now().year, lookback_sprints = 3) -> str:

        if not team_id:
            return json.dumps({"error": "team_id is required"})

        teams = data.get("teams", [])
        sprints = data.get("sprints", [])
        budgets = data.get("budgets", [])
        expenses = data.get("expenses", [])
        task_logs = data.get("task_logs", [])
        employees = list(data.get("employees", {}).values())

        team = next((t for t in teams if t.get("team_id") == team_id), None)
        if not team:
            return json.dumps({"error": f"Team {team_id} not found"})

        team_sprints = [
            s
            for s in sprints
            if s.get("team_id") == team_id and s.get("status") == "completed"
        ]

        team_sprints.sort(key=lambda x: x.get("end_date", ""), reverse=True)
        recent_sprints = team_sprints[:lookback_sprints]

        if not recent_sprints:
            return json.dumps({"error": "No completed sprints found for team"})

        sprint_metrics = []
        total_velocity = 0
        total_cost = 0

        for sprint in recent_sprints:
            sprint_velocity = sprint.get("velocity", 0)
            total_velocity += sprint_velocity

            sprint_cost = 0

            start_date = datetime.fromisoformat(
                sprint["start_date"].replace("Z", "+00:00")
            )
            end_date = datetime.fromisoformat(sprint["end_date"].replace("Z", "+00:00"))
            duration_weeks = (end_date - start_date).days / 7

            for member_id in team.get("members", []):
                employee = next(
                    (e for e in employees if e.get("employee_id") == member_id), None
                )
                if employee:
                    hourly_rate = (
                        150 if "senior" in employee.get("role", "").lower() else 100
                    )

                    member_cost = hourly_rate * 40 * duration_weeks
                    sprint_cost += member_cost

            sprint_expenses = [
                e
                for e in expenses
                if e.get("sprint_id") == sprint["sprint_id"]
                and e.get("status") == "approved"
            ]
            sprint_expense_total = sum(e.get("amount", 0) for e in sprint_expenses)
            sprint_cost += sprint_expense_total

            total_cost += sprint_cost

            sprint_metrics.append(
                {
                    "sprint_id": sprint["sprint_id"],
                    "sprint_name": sprint["sprint_name"],
                    "velocity": sprint_velocity,
                    "cost": sprint_cost,
                    "cost_per_point": round(sprint_cost / sprint_velocity, 2)
                    if sprint_velocity > 0
                    else 0,
                    "duration_weeks": round(duration_weeks, 1),
                }
            )

        project_id = team.get("project_id")
        budget = next(
            (
                b
                for b in budgets
                if b.get("project_id") == project_id
                and b.get("fiscal_year") == fiscal_year
            ),
            None,
        )

        avg_velocity = total_velocity / len(recent_sprints)
        avg_cost_per_sprint = total_cost / len(recent_sprints)
        avg_cost_per_point = total_cost / total_velocity if total_velocity > 0 else 0

        remaining_budget = 0
        if budget:
            remaining_budget = budget["total_budget"] - budget.get("spent_amount", 0)

        projected_sprints_remaining = (
            remaining_budget / avg_cost_per_sprint if avg_cost_per_sprint > 0 else 0
        )
        projected_story_points = projected_sprints_remaining * avg_velocity

        analysis = {
            "projected_sprints_remaining": round(projected_sprints_remaining, 1),
            "team_id": team_id,
            "team_name": team["team_name"],
            "analysis_period": {
                "sprints_analyzed": len(recent_sprints),
                "total_story_points": total_velocity,
                "total_cost": total_cost,
            },
            "velocity_metrics": {
                "average_velocity": round(avg_velocity, 2),
                "velocity_trend": "improving"
                if len(sprint_metrics) > 1
                and sprint_metrics[0]["velocity"] > sprint_metrics[-1]["velocity"]
                else "stable",
            },
            "cost_metrics": {
                "average_cost_per_sprint": round(avg_cost_per_sprint, 2),
                "average_cost_per_story_point": round(avg_cost_per_point, 2),
                "cost_efficiency_trend": "improving"
                if len(sprint_metrics) > 1
                and sprint_metrics[0]["cost_per_point"]
                < sprint_metrics[-1]["cost_per_point"]
                else "stable",
            },
            "budget_projection": {
                "remaining_budget": remaining_budget,
                "projected_sprints_remaining": round(projected_sprints_remaining, 1),
                "projected_story_points_deliverable": round(projected_story_points, 0),
            },
            "sprint_breakdown": sprint_metrics,
            "recommendations": [],
        }

        if avg_cost_per_point > 1000:
            analysis["recommendations"].append(
                "High cost per story point - consider efficiency improvements"
            )
        if projected_sprints_remaining < 2:
            analysis["recommendations"].append(
                "Budget running low - consider requesting budget modification"
            )

        return json.dumps(analysis, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "calculate_velocity_budget_ratio",
                "description": "Calculate team velocity to budget ratio and project future capacity",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "team_id": {"type": "string", "description": "Team ID"},
                        "lookback_sprints": {
                            "type": "integer",
                            "description": "Number of sprints to analyze",
                        },
                        "fiscal_year": {
                            "type": "integer",
                            "description": "Fiscal year (defaults to current)",
                        },
                    },
                    "required": ["team_id"],
                },
            },
        }
