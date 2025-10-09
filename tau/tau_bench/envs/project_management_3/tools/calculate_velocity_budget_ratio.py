from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime, timezone
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class CalculateVelocityBudgetRatio(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any], 
        team_id: str, 
        lookback_sprints: int = 3, 
        fiscal_year: int = datetime.now().year
    ) -> str:
        if not team_id:
            payload = {"error": "team_id is required"}
            out = json.dumps(payload)
            return out

        teams = data.get("teams", {}).values()
        sprints = data.get("sprints", {}).values()
        budgets = data.get("budgets", {}).values()
        expenses = data.get("expenses", {}).values()
        data.get("task_logs", {}).values()
        employees = data.get("employees", {}).values()

        team = next((t for t in teams.values() if t.get("team_id") == team_id), None)
        if not team:
            payload = {"error": f"Team {team_id} not found"}
            out = json.dumps(payload)
            return out

        team_sprints = [
            s
            for s in sprints.values() if s.get("team_id") == team_id and s.get("status") == "completed"
        ]

        team_sprints.sort(key=lambda x: x.get("end_date", ""), reverse=True)
        recent_sprints = team_sprints[:lookback_sprints]

        if not recent_sprints:
            payload = {"error": "No completed sprints found for team"}
            out = json.dumps(payload)
            return out

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
                    (e for e in employees.values() if e.get("employee_id") == member_id), None
                )
                if employee:
                    hourly_rate = (
                        150 if "senior" in employee.get("role", "").lower() else 100
                    )

                    member_cost = hourly_rate * 40 * duration_weeks
                    sprint_cost += member_cost

            sprint_expenses = [
                e
                for e in expenses.values() if e.get("sprint_id") == sprint["sprint_id"]
                and e.get("status") == "approved"
            ]
            sprint_expense_total = sum(e.get("amount", 0) for e in sprint_expenses.values())
            sprint_cost += sprint_expense_total

            total_cost += sprint_cost

            sprint_metrics.append(
                {
                    "sprint_id": sprint["sprint_id"],
                    "sprint_name": sprint["sprint_name"],
                    "velocity": sprint_velocity,
                    "cost": sprint_cost,
                    "cost_per_point": (
                        round(sprint_cost / sprint_velocity, 2)
                        if sprint_velocity > 0
                        else 0
                    ),
                    "duration_weeks": round(duration_weeks, 1),
                }
            )

        project_id = team.get("project_id")
        budget = next(
            (
                b
                for b in budgets.values() if b.get("project_id") == project_id
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
                "velocity_trend": (
                    "improving"
                    if len(sprint_metrics) > 1
                    and sprint_metrics[0]["velocity"] > sprint_metrics[-1]["velocity"]
                    else "stable"
                ),
            },
            "cost_metrics": {
                "average_cost_per_sprint": round(avg_cost_per_sprint, 2),
                "average_cost_per_story_point": round(avg_cost_per_point, 2),
                "cost_efficiency_trend": (
                    "improving"
                    if len(sprint_metrics) > 1
                    and sprint_metrics[0]["cost_per_point"]
                    < sprint_metrics[-1]["cost_per_point"]
                    else "stable"
                ),
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
        payload = analysis
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CalculateVelocityBudgetRatio",
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
