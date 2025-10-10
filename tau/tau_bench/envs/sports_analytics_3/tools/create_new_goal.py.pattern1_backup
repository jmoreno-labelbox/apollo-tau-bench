# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateNewGoal(Tool):
    """
    Create a new player development goal.
    Required:
      - dev_report_id
      - player_id
      - goal_text
      - coach_id
      - target_review_date (YYYY-MM-DD)
    Defaults:
      - goal_id auto-generated
      - goal_status = "Active"
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        dev_report_id = kwargs.get("dev_report_id")
        player_id = kwargs.get("player_id")
        goal_text = kwargs.get("goal_text")
        coach_id = kwargs.get("coach_id")
        target_review_date = kwargs.get("target_review_date")

        # Validate required
        missing = []
        for field, val in [
            ("dev_report_id", dev_report_id),
            ("player_id", player_id),
            ("goal_text", goal_text if isinstance(goal_text, str) and goal_text.strip() else None),
            ("coach_id", coach_id),
            ("target_review_date", target_review_date if isinstance(target_review_date, str) and target_review_date.strip() else None),
        ]:
            if val is None:
                missing.append(field)

        if missing:
            return json.dumps({"error": f"Missing required field(s): {', '.join(missing)}"}, indent=2)

        goals: List[Dict[str, Any]] = data.get("player_dev_goals", [])


        new_goal = {
            "goal_id": get_next_player_goal_id(data),
            "dev_report_id": dev_report_id,
            "player_id": player_id,
            "goal_text": goal_text,
            "goal_status": "Active",
            "coach_id": coach_id,
            "target_review_date": target_review_date
        }
        goals.append(new_goal)

        return json.dumps(new_goal, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_new_goal",
                "description": "Create a new player development goal. goal_id auto-generated; goal_status defaults to 'Active'.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "dev_report_id": {
                            "type": "integer",
                            "description": "Development report ID associated with the goal."
                        },
                        "player_id": {
                            "type": "integer",
                            "description": "Player ID the goal is for."
                        },
                        "goal_text": {
                            "type": "string",
                            "description": "Description of the development goal."
                        },
                        "coach_id": {
                            "type": "integer",
                            "description": "Coach ID who set the goal."
                        },
                        "target_review_date": {
                            "type": "string",
                            "description": "Target review date in YYYY-MM-DD."
                        }
                    },
                    "required": ["dev_report_id", "player_id", "goal_text", "coach_id", "target_review_date"]
                }
            }
        }
