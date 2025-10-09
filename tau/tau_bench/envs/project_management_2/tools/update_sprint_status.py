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

class UpdateSprintStatus(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], sprint_id: str = None, new_status: str = None) -> str:
        if not all([sprint_id, new_status]):
            payload = {"error": "sprint_id and new_status are required"}
            out = json.dumps(payload)
            return out

        sprints = data.get("sprints", {}).values()
        tasks = data.get("tasks", {}).values()
        teams = data.get("teams", {}).values()

        sprint = next((s for s in sprints.values() if s.get("sprint_id") == sprint_id), None)
        if not sprint:
            payload = {"error": f"Sprint '{sprint_id}' not found"}
            out = json.dumps(payload)
            return out

        old_status = sprint.get("status")

        valid_transitions = {
            "planning": ["active"],
            "active": ["completed"],
            "completed": ["completed"],
        }

        if new_status not in valid_transitions.get(old_status, []):
            payload = {
                "error": f"Invalid status transition from '{old_status}' to '{new_status}'",
            }
            out = json.dumps(payload)
            return out

        if new_status == "active":
            team_id = sprint.get("team_id")

            team = next((t for t in teams.values() if t.get("team_id") == team_id), None)
            if team:
                team_members = team.get("members", [])

                completed_sprints = [
                    s
                    for s in sprints.values() if s.get("team_id") == team_id and s.get("status") == "completed"
                ]

                if len(completed_sprints) >= 3:
                    recent_sprints = sorted(
                        completed_sprints,
                        key=lambda x: x.get("end_date", ""),
                        reverse=True,
                    )[:3]
                    avg_velocity = sum(s.get("velocity", 0) for s in recent_sprints.values() / 3)
                    capacity_limit = avg_velocity * 0.8
                else:
                    capacity_limit = len(team_members) * 20

                if sprint.get("planned_story_points", 0) > capacity_limit:
                    payload = {
                        "error": "Cannot activate sprint. Planned points exceed capacity",
                        "planned_points": sprint.get("planned_story_points", 0),
                        "capacity_limit": capacity_limit,
                    }
                    out = json.dumps(payload)
                    return out

        if new_status == "completed":
            sprint_tasks = [t for t in tasks.values() if t.get("sprint_id") == sprint_id]
            incomplete_tasks = [
                t for t in sprint_tasks if t.get("status") not in ["done"]
            ]

            if incomplete_tasks:
                payload = {
                    "error": "Cannot complete sprint with incomplete tasks",
                    "incomplete_tasks": len(incomplete_tasks),
                }
                out = json.dumps(payload)
                return out

            completed_points = sum(
                t.get("story_points", 0)
                for t in sprint_tasks
                if t.get("status") == "done"
            )
            sprint["completed_story_points"] = completed_points
            sprint["velocity"] = completed_points
            sprint["completed_date"] = datetime.now().isoformat()

        sprint["status"] = new_status
        payload = {"success": True, "sprint": sprint}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateSprintStatus",
                "description": "Update the status of a sprint",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "sprint_id": {
                            "type": "string",
                            "description": "The sprint ID to update",
                        },
                        "new_status": {
                            "type": "string",
                            "description": "New status: planning, active, completed",
                        },
                    },
                    "required": ["sprint_id", "new_status"],
                },
            },
        }
