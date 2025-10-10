# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateGoal(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any],
        user_id: str,
        goal_id: str,
        last_updated_date: str,
        status: str = None,
        progress_percent: int = None,
        notes_to_append: str = None,
    ) -> str:
        goals_data = data.get("goals", [])
        user_goals_obj = next(
            (g for g in goals_data if g.get("user_id") == user_id), None
        )
        if not user_goals_obj:
            return json.dumps(
                {"error": f"User {user_id} not found in goals data"}, indent=2
            )

        goal_to_update = next(
            (g for g in user_goals_obj.get("goals", []) if g.get("goal_id") == goal_id),
            None,
        )

        if not goal_to_update:
            return json.dumps(
                {"error": f"Goal {goal_id} not found for user {user_id}"}, indent=2
            )

        # Apply updates if provided
        if status is not None:
            goal_to_update["status"] = status
        if progress_percent is not None:
            goal_to_update["progress_percent"] = progress_percent
        if notes_to_append:
            existing_notes = goal_to_update.get("notes", "")
            if existing_notes:
                goal_to_update["notes"] = f"{existing_notes} {notes_to_append}".strip()
            else:
                goal_to_update["notes"] = notes_to_append.strip()

        # Set the last_updated date from the provided parameter
        goal_to_update["last_updated"] = last_updated_date

        return json.dumps(
            {"success": f"Goal {goal_id} updated for user {user_id}"}, indent=2
        )

    @staticmethod
    def get_info() -> dict:
        return {
            "type": "function",
            "function": {
                "name": "update_goal",
                "description": "Update specific fields of a user's goal. The last_updated date must be provided.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "user_id": {
                            "type": "string",
                            "description": "The ID of the user whose goal is to be updated.",
                        },
                        "goal_id": {
                            "type": "string",
                            "description": "The ID of the goal to update.",
                        },
                        "last_updated_date": {
                            "type": "string",
                            "description": "The date of the update in YYYY-MM-DD format. Typically sourced from the get_today_date tool.",
                        },
                        "status": {
                            "type": "string",
                            "description": "The new status for the goal (e.g., 'Active', 'Completed').",
                        },
                        "progress_percent": {
                            "type": "integer",
                            "description": "The new progress percentage (0-100).",
                        },
                        "notes_to_append": {
                            "type": "string",
                            "description": "A string of text to append to the existing notes.",
                        },
                    },
                    "required": ["user_id", "goal_id", "last_updated_date"],
                },
            },
        }
