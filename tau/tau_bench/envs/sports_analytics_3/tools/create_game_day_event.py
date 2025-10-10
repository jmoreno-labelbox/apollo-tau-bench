# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateGameDayEvent(Tool):
    """
    Create a new game-day event.
    Inputs (exact names):
      - game_pk (int) [required]
      - pitch_id (int) [required]
      - leverage_index (float or int) [required]
      - is_manual_alert (bool) [required]
      - suggestion_text (string) [required]
    Behavior:
      - event_id is generated automatically (max existing event_id + 1; starts at 1 if empty).
      - draft_status defaults to "Draft".
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        game_pk = kwargs.get("game_pk")
        pitch_id = kwargs.get("pitch_id")
        leverage_index = kwargs.get("leverage_index")
        is_manual_alert = kwargs.get("is_manual_alert")
        suggestion_text = kwargs.get("suggestion_text")

        # 1) Verify mandatory inputs
        missing = []
        if game_pk is None:
            missing.append("game_pk")
        if leverage_index is None:
            missing.append("leverage_index")
        if is_manual_alert is None:
            missing.append("is_manual_alert")
        if not isinstance(suggestion_text, str) or suggestion_text == "":
            missing.append("suggestion_text")

        if missing:
            return json.dumps({"error": f"Missing required field(s): {', '.join(missing)}"}, indent=2)

        # Retrieve database.
        events: List[Dict[str, Any]] = list(data.get("game_day_events", {}).values())

        # 4) Add a new event entry
        new_event = {
            "event_id": get_next_event_id(data),
            "game_pk": game_pk,
            "pitch_id": pitch_id,
            "timestamp_utc": get_current_timestamp(),  # May be populated later if required.
            "leverage_index": leverage_index,
            "is_manual_alert": is_manual_alert,
            "suggestion_text": suggestion_text,
            "draft_status": "draft"
        }

        # 5) Add to database
        events.append(new_event)

        return json.dumps(new_event, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_game_day_event",
                "description": (
                    "Create a new game-day event. event_id is generated automatically "
                    "(max existing + 1). draft_status defaults to 'Draft'."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "game_pk": {
                            "type": "integer",
                            "description": "Game primary key this event belongs to."
                        },
                        "pitch_id": {
                            "type": "integer",
                            "description": "Pitch ID associated with the event."
                        },
                        "leverage_index": {
                            "type": "number",
                            "description": "Leverage index for the event."
                        },
                        "is_manual_alert": {
                            "type": "boolean",
                            "description": "True if the alert is manually triggered, else False."
                        },
                        "suggestion_text": {
                            "type": "string",
                            "description": "Suggestion text for the event."
                        }
                    },
                    "required": [
                        "game_pk",
                        "leverage_index",
                        "is_manual_alert",
                        "suggestion_text"
                    ]
                }
            }
        }
