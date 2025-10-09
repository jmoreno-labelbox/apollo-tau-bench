from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class UpdateGameEventStatus(Tool):
    """
    Modify the draft_status of a current game-day event.

    Inputs:
      - event_id (int) [required]
      - draft_status (string) [required]
    """

    @staticmethod
    def invoke(data: dict[str, Any], event_id: str = None, draft_status: str = None) -> str:
        #1) Confirm validity
        if event_id is None:
            payload = {"error": "Missing required field: event_id"}
            out = json.dumps(payload, indent=2)
            return out
        if not isinstance(draft_status, str) or draft_status == "":
            payload = {"error": "Missing required field: draft_status"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        #2) Retrieve DB
        events: list[dict[str, Any]] = data.get("game_day_events", [])

        #3) Locate and modify
        for event in events:
            if event.get("event_id") == event_id:
                event["draft_status"] = draft_status
                payload = event
                out = json.dumps(payload, indent=2)
                return out
        payload = {"error": f"No event found with event_id {event_id}"}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "updateGameEventStatus",
                "description": "Update the draft_status of a game-day event identified by event_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "event_id": {
                            "type": "integer",
                            "description": "Exact event ID to update.",
                        },
                        "draft_status": {
                            "type": "string",
                            "description": "New draft status for the event (e.g., 'draft', 'published', 'archived').",
                        },
                    },
                    "required": ["event_id", "draft_status"],
                },
            },
        }
