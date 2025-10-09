from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class UpdateGoal(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
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
            payload = {"error": f"User {user_id} not found in goals data"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        goal_to_update = next(
            (g for g in user_goals_obj.get("goals", []) if g.get("goal_id") == goal_id),
            None,
        )

        if not goal_to_update:
            payload = {"error": f"Goal {goal_id} not found for user {user_id}"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        # Implement updates if supplied
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

        # Assign the last_updated date based on the supplied parameter
        goal_to_update["last_updated"] = last_updated_date
        payload = {"success": f"Goal {goal_id} updated for user {user_id}"}
        out = json.dumps(
            payload, indent=2
        )
        return out
            

    @staticmethod
    def get_info() -> dict:
        pass
        return {
            "type": "function",
            "function": {
                "name": "UpdateGoal",
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
