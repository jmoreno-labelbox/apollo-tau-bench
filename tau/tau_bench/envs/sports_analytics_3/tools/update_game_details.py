# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateGameDetails(Tool):
    """
    Update a game's details using exact input names:
      - Required: gamepk
      - Optional (at least one must be provided): status, score, attendance

    Business rule:
      - final_score ("score") and attendance can be changed ONLY when the game's
        resulting status is 'Final'. This means:
          * If you pass score/attendance without passing status, the current game
            status must already be 'Final'.
          * If you pass status together with score/attendance, that status must be
            'Final' in the same request.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        gamepk = kwargs.get("gamepk")
        status = kwargs.get("status")
        score = kwargs.get("score")
        attendance = kwargs.get("attendance")

        # 1) Validate presence
        if gamepk is None:
            return json.dumps({"error": "Missing required field: gamepk"}, indent=2)

        if status is None and score is None and attendance is None:
            return json.dumps(
                {"error": "At least one of status, score, or attendance must be provided"},
                indent=2
            )

        # 2) Get DB
        games: List[Dict[str, Any]] = data.get("games", [])

        # 3) Find the game
        target = None
        for game in games:
            if game.get("game_pk") == gamepk:
                target = game
                break

        if target is None:
            return json.dumps({"error": f"No game found with game_pk {gamepk}"}, indent=2)

        # 4) Enforce business rule about 'Final' status for score/attendance
        # Determine the resulting status after this update
        resulting_status = status if status is not None else target.get("game_status")

        # If trying to change score/attendance, resulting status must be 'Final'
        wants_score_or_attendance_change = (score is not None) or (attendance is not None)
        if wants_score_or_attendance_change and resulting_status != "Final":
            return json.dumps(
                {"error": "Cannot change score or attendance unless the game status is 'Final' "
                          "(either already Final or set to 'Final' in this request)."},
                indent=2
            )

        # 5) Apply updates deterministically (only provided fields)
        if status is not None:
            target["game_status"] = status
        if score is not None:
            target["final_score"] = score
        if attendance is not None:
            target["attendance"] = attendance

        return json.dumps(target, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_game_details",
                "description": (
                    "Update a game's status, score, and/or attendance by exact gamepk. "
                    "At least one of the optional fields must be provided. "
                    "Score and attendance may only be changed when the resulting status is 'Final'."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "gamepk": {
                            "type": "integer",
                            "description": "Exact game primary key to update."
                        },
                        "status": {
                            "type": ["string", "null"],
                            "description": "New game status (e.g., 'Scheduled', 'Final', 'Postponed') or null."
                        },
                        "score": {
                            "type": ["string", "null"],
                            "description": "New final score text (e.g., '5-3') or null. "
                                           "Can only be changed when status is 'Final'."
                        },
                        "attendance": {
                            "type": ["integer", "null"],
                            "description": "New attendance value or null. "
                                           "Can only be changed when status is 'Final'."
                        }
                    },
                    "required": ["gamepk"]
                }
            }
        }
