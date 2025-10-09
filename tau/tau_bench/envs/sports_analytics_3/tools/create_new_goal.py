from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class CreateNewGoal(Tool):
    """
    Establish a new player development goal.
    Required:
      - dev_report_id
      - player_id
      - goal_text
      - coach_id
      - target_review_date (YYYY-MM-DD)
    Defaults:
      - goal_id is auto-generated
      - goal_status = "Active"
    """

    @staticmethod
    def invoke(
        data: dict[str, Any],
        dev_report_id: str = None,
        player_id: str = None,
        goal_text: str = None,
        coach_id: str = None,
        target_review_date: str = None
    ) -> str:
        # Confirm required
        missing = []
        for field, val in [
            ("dev_report_id", dev_report_id),
            ("player_id", player_id),
            (
                "goal_text",
                goal_text if isinstance(goal_text, str) and goal_text.strip() else None,
            ),
            ("coach_id", coach_id),
            (
                "target_review_date",
                (
                    target_review_date
                    if isinstance(target_review_date, str)
                    and target_review_date.strip()
                    else None
                ),
            ),
        ]:
            if val is None:
                missing.append(field)

        if missing:
            payload = {"error": f"Missing required field(s): {', '.join(missing)}"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        goals: list[dict[str, Any]] = data.get("player_dev_goals", {}).values()

        new_goal = {
            "goal_id": get_next_player_goal_id(data),
            "dev_report_id": dev_report_id,
            "player_id": player_id,
            "goal_text": goal_text,
            "goal_status": "Active",
            "coach_id": coach_id,
            "target_review_date": target_review_date,
        }
        goals.append(new_goal)
        payload = new_goal
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "CreateNewGoal",
                "description": "Create a new player development goal. goal_id auto-generated; goal_status defaults to 'Active'.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "dev_report_id": {
                            "type": "integer",
                            "description": "Development report ID associated with the goal.",
                        },
                        "player_id": {
                            "type": "integer",
                            "description": "Player ID the goal is for.",
                        },
                        "goal_text": {
                            "type": "string",
                            "description": "Description of the development goal.",
                        },
                        "coach_id": {
                            "type": "integer",
                            "description": "Coach ID who set the goal.",
                        },
                        "target_review_date": {
                            "type": "string",
                            "description": "Target review date in YYYY-MM-DD.",
                        },
                    },
                    "required": [
                        "dev_report_id",
                        "player_id",
                        "goal_text",
                        "coach_id",
                        "target_review_date",
                    ],
                },
            },
        }
