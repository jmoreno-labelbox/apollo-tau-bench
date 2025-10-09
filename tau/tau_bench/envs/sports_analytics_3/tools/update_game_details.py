from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class UpdateGameDetails(Tool):
    """
    Modify a game's details using exact input names:
      - Required: gamepk
      - Optional (at least one must be provided): status, score, attendance

    Business rule:
      - final_score ("score") and attendance can only be modified when the game's
        resulting status is 'Final'. This implies:
          * If you provide score/attendance without status, the current game
            status must already be 'Final'.
          * If you provide status along with score/attendance, that status must be
            'Final' in the same request.
    """

    @staticmethod
    def invoke(data: dict[str, Any], gamepk: int = None, status: str = None, score: int = None, attendance: int = None) -> str:
        #1) Confirm presence
        if gamepk is None:
            payload = {"error": "Missing required field: gamepk"}
            out = json.dumps(payload, indent=2)
            return out

        if status is None and score is None and attendance is None:
            payload = {
                    "error": "At least one of status, score, or attendance must be provided"
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        #2) Retrieve DB
        games: list[dict[str, Any]] = data.get("games", {}).values()

        #3) Locate the game
        target = None
        for game in games:
            if game.get("game_pk") == gamepk:
                target = game
                break

        if target is None:
            payload = {"error": f"No game found with game_pk {gamepk}"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        #4) Apply business rule regarding 'Final' status for score/attendance
        #Establish the resulting status following this update
        resulting_status = status if status is not None else target.get("game_status")

        #If attempting to modify score/attendance, the resulting status must be 'Final'
        wants_score_or_attendance_change = (score is not None) or (
            attendance is not None
        )
        if wants_score_or_attendance_change and resulting_status != "Final":
            payload = {
                    "error": "Cannot change score or attendance unless the game status is 'Final' "
                    "(either already Final or set to 'Final' in this request)."
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        #5) Implement updates in a deterministic manner (only specified fields)
        if status is not None:
            target["game_status"] = status
        if score is not None:
            target["final_score"] = score
        if attendance is not None:
            target["attendance"] = attendance
        payload = target
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "updateGameDetails",
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
                            "description": "Exact game primary key to update.",
                        },
                        "status": {
                            "type": ["string", "null"],
                            "description": "New game status (e.g., 'Scheduled', 'Final', 'Postponed') or null.",
                        },
                        "score": {
                            "type": ["string", "null"],
                            "description": "New final score text (e.g., '5-3') or null. "
                            "Can only be changed when status is 'Final'.",
                        },
                        "attendance": {
                            "type": ["integer", "null"],
                            "description": "New attendance value or null. "
                            "Can only be changed when status is 'Final'.",
                        },
                    },
                    "required": ["gamepk"],
                },
            },
        }
