# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateGameEventStatus(Tool):
    """
    Update the draft_status of an existing game-day event.

    Inputs:
      - event_id (int) [required]
      - draft_status (string) [required]
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        event_id = kwargs.get("event_id")
        draft_status = kwargs.get("draft_status")

        # 1) Validate
        if event_id is None:
            return json.dumps({"error": "Missing required field: event_id"}, indent=2)
        if not isinstance(draft_status, str) or draft_status == "":
            return json.dumps({"error": "Missing required field: draft_status"}, indent=2)

        # 2) Get DB
        events: List[Dict[str, Any]] = data.get("game_day_events", [])

        # 3) Find and update
        for event in events:
            if event.get("event_id") == event_id:
                event["draft_status"] = draft_status
                return json.dumps(event, indent=2)

        return json.dumps({"error": f"No event found with event_id {event_id}"}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_game_event_status",
                "description": "Update the draft_status of a game-day event identified by event_id.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "event_id": {
                            "type": "integer",
                            "description": "Exact event ID to update."
                        },
                        "draft_status": {
                            "type": "string",
                            "description": "New draft status for the event (e.g., 'draft', 'published', 'archived')."
                        }
                    },
                    "required": ["event_id", "draft_status"]
                }
            }
        }
