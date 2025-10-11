# Copyright Sierra

import datetime
import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateSprintStatus(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], new_status, sprint_id) -> str:

        if not all([sprint_id, new_status]):
            return json.dumps({"error": "sprint_id and new_status are required"})

        sprints = list(data.get("sprints", {}).values())
        tasks = list(data.get("tasks", {}).values())
        teams = list(data.get("teams", {}).values())

        sprint = next((s for s in sprints if s.get("sprint_id") == sprint_id), None)
        if not sprint:
            return json.dumps({"error": f"Sprint '{sprint_id}' not found"})

        old_status = sprint.get("status")

        valid_transitions = {
            "planning": ["active"],
            "active": ["completed"],
            "completed": ["completed"],
        }

        if new_status not in valid_transitions.get(old_status, []):
            return json.dumps(
                {
                    "error": f"Invalid status transition from '{old_status}' to '{new_status}'",
                }
            )

        if new_status == "active":
            team_id = sprint.get("team_id")

            team = next((t for t in teams if t.get("team_id") == team_id), None)
            if team:
                team_members = team.get("members", [])

                completed_sprints = [
                    s
                    for s in sprints
                    if s.get("team_id") == team_id and s.get("status") == "completed"
                ]

                if len(completed_sprints) >= 3:
                    recent_sprints = sorted(
                        completed_sprints,
                        key=lambda x: x.get("end_date", ""),
                        reverse=True,
                    )[:3]
                    avg_velocity = sum(s.get("velocity", 0) for s in recent_sprints) / 3
                    capacity_limit = avg_velocity * 0.8
                else:
                    capacity_limit = len(team_members) * 20

                if sprint.get("planned_story_points", 0) > capacity_limit:
                    return json.dumps(
                        {
                            "error": "Cannot activate sprint. Planned points exceed capacity",
                            "planned_points": sprint.get("planned_story_points", 0),
                            "capacity_limit": capacity_limit,
                        }
                    )

        if new_status == "completed":

            sprint_tasks = [t for t in tasks if t.get("sprint_id") == sprint_id]
            incomplete_tasks = [
                t for t in sprint_tasks if t.get("status") not in ["done"]
            ]

            if incomplete_tasks:
                return json.dumps(
                    {
                        "error": "Cannot complete sprint with incomplete tasks",
                        "incomplete_tasks": len(incomplete_tasks),
                    }
                )

            completed_points = sum(
                t.get("story_points", 0)
                for t in sprint_tasks
                if t.get("status") == "done"
            )
            sprint["completed_story_points"] = completed_points
            sprint["velocity"] = completed_points
            sprint["completed_date"] = datetime.datetime.now().isoformat()

        sprint["status"] = new_status
        return json.dumps({"success": True, "sprint": sprint})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_sprint_status",
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
