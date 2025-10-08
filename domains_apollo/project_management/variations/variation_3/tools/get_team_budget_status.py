from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime, timezone
from typing import Any

class GetTeamBudgetStatus(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any], 
        team_id: str, 
        include_member_breakdown: bool = False, 
        fiscal_year: int = datetime.now().year
    ) -> str:
        if not team_id:
            payload = {"error": "team_id is required"}
            out = json.dumps(payload)
            return out

        teams = data.get("teams", [])
        budgets = data.get("budgets", [])
        expenses = data.get("expenses", [])
        employees = data.get("employees", [])
        task_logs = data.get("task_logs", [])

        team = next((t for t in teams if t.get("team_id") == team_id), None)
        if not team:
            payload = {"error": f"Team {team_id} not found"}
            out = json.dumps(payload)
            return out

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

        if not budget:
            payload = {"error": f"No budget found for team's project {project_id}"}
            out = json.dumps(payload)
            return out

        team_members = team.get("members", [])
        member_costs = {}
        total_team_cost = 0

        for member_id in team_members:
            employee = next(
                (e for e in employees if e.get("employee_id") == member_id), None
            )
            if employee:
                hourly_rate = (
                    150 if "senior" in employee.get("role", "").lower() else 100
                )
                if "lead" in employee.get("role", "").lower():
                    hourly_rate = 175

                member_logs = [
                    log for log in task_logs if log.get("employee_id") == member_id
                ]
                total_hours = sum(log.get("hours", 0) for log in member_logs)
                member_cost = total_hours * hourly_rate

                member_costs[member_id] = {
                    "name": employee.get("name"),
                    "role": employee.get("role"),
                    "hourly_rate": hourly_rate,
                    "logged_hours": total_hours,
                    "total_cost": member_cost,
                }
                total_team_cost += member_cost

        team_expenses = [
            e
            for e in expenses
            if e.get("employee_id") in team_members
            and e.get("project_id") == project_id
            and e.get("status") == "approved"
        ]

        total_expenses = sum(e.get("amount", 0) for e in team_expenses)

        status = {
            "budget_utilization": (
                round((total_team_cost / budget["personnel_budget"] * 100), 2)
                if budget["personnel_budget"] > 0
                else 0
            ),
            "team_id": team_id,
            "team_name": team.get("team_name"),
            "project_id": project_id,
            "budget_info": {
                "total_budget": budget["total_budget"],
                "personnel_budget": budget["personnel_budget"],
                "spent_amount": budget.get("spent_amount", 0),
                "available_amount": budget["total_budget"]
                - budget.get("spent_amount", 0),
            },
            "team_costs": {
                "personnel_cost": total_team_cost,
                "expense_cost": total_expenses,
                "total_cost": total_team_cost + total_expenses,
            },
            "cost_efficiency": {
                "cost_per_member": (
                    total_team_cost / len(team_members) if team_members else 0
                ),
                "budget_utilization": (
                    round((total_team_cost / budget["personnel_budget"] * 100), 2)
                    if budget["personnel_budget"] > 0
                    else 0
                ),
            },
        }

        if include_member_breakdown:
            status["member_breakdown"] = member_costs

        if status["cost_efficiency"]["budget_utilization"] > 80:
            status["warning"] = "Team personnel costs approaching budget limit"
        payload = status
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetTeamBudgetStatus",
                "description": "Get budget status and cost breakdown for a team",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "team_id": {"type": "string", "description": "Team ID"},
                        "include_member_breakdown": {
                            "type": "boolean",
                            "description": "Include individual member costs",
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
