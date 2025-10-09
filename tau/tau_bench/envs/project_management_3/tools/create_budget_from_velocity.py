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

class CreateBudgetFromVelocity(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], project_id: str, target_story_points: int, buffer_percentage: int = 20) -> str:
        if not all([project_id, target_story_points]):
            payload = {"error": "project_id and target_story_points are required"}
            out = json.dumps(payload)
            return out

        projects = data.get("projects", {}).values()
        teams = data.get("teams", {}).values()
        sprints = data.get("sprints", {}).values()
        budgets = data.get("budgets", {}).values()
        employees = data.get("employees", {}).values()

        project = next((p for p in projects.values() if p.get("project_id") == project_id), None)
        if not project:
            payload = {"error": f"Project {project_id} not found"}
            out = json.dumps(payload)
            return out

        project_team = next(
            (t for t in teams.values() if t.get("project_id") == project_id), None
        )
        if not project_team:
            payload = {"error": "No team assigned to project"}
            out = json.dumps(payload)
            return out

        team_sprints = [
            s
            for s in sprints.values() if s.get("team_id") == project_team["team_id"]
            and s.get("status") == "completed"
        ]

        if not team_sprints:
            avg_velocity = 40
            avg_cost_per_point = 500
        else:
            total_velocity = sum(s.get("velocity", 0) for s in team_sprints.values()
            total_sprints = len(team_sprints)
            avg_velocity = total_velocity / total_sprints if total_sprints > 0 else 40

            total_cost = 0
            for member_id in project_team.get("members", []):
                employee = next(
                    (e for e in employees.values() if e.get("employee_id") == member_id), None
                )
                if employee:
                    hourly_rate = (
                        150 if "senior" in employee.get("role", "").lower() else 100
                    )

                    total_cost += hourly_rate * 80 * total_sprints

            avg_cost_per_point = (
                total_cost / total_velocity if total_velocity > 0 else 500
            )

        required_sprints = target_story_points / avg_velocity if avg_velocity > 0 else 1
        base_budget = target_story_points * avg_cost_per_point

        total_budget = base_budget * (1 + buffer_percentage / 100)

        budget_id = f"budget_{uuid.uuid4().hex[:8]}"

        new_budget = {
            "budget_id": budget_id,
            "project_id": project_id,
            "fiscal_year": datetime.now().year,
            "total_budget": round(total_budget, 2),
            "personnel_budget": round(total_budget * 0.8, 2),
            "non_personnel_budget": round(total_budget * 0.2, 2),
            "calculation_basis": {
                "target_story_points": target_story_points,
                "average_velocity": round(avg_velocity, 2),
                "required_sprints": round(required_sprints, 1),
                "cost_per_story_point": round(avg_cost_per_point, 2),
                "buffer_percentage": buffer_percentage,
            },
            "spent_amount": 0,
            "committed_amount": 0,
            "status": "active",
            "created_date": datetime.now().isoformat(),
            "department": project.get("department"),
        }

        data["budgets"][budget_id] = new_budget
        payload = {"success": True, "budget": new_budget}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateBudgetFromVelocity",
                "description": "Create project budget based on team velocity and story point targets",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "project_id": {"type": "string", "description": "Project ID"},
                        "target_story_points": {
                            "type": "integer",
                            "description": "Total story points to deliver",
                        },
                        "buffer_percentage": {
                            "type": "integer",
                            "description": "Budget buffer percentage (default 20%)",
                        },
                    },
                    "required": ["project_id", "target_story_points"],
                },
            },
        }
