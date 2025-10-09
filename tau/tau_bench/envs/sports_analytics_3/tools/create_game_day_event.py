from tau_bench.envs.tool import Tool
import json
from typing import Any

class CreateGameDayEvent(Tool):
    """
    Establish a new game-day event.
    Inputs (exact names):
      - game_pk (int) [required]
      - pitch_id (int) [required]
      - leverage_index (float or int) [required]
      - is_manual_alert (bool) [required]
      - suggestion_text (string) [required]
    Behavior:
      - event_id is automatically generated (max existing event_id + 1; starts at 1 if none).
      - draft_status defaults to "Draft".
    """

    @staticmethod
    def invoke(
        data: dict[str, Any],
        game_pk: int = None,
        pitch_id: int = None,
        leverage_index: float = None,
        is_manual_alert: bool = None,
        suggestion_text: str = None
    ) -> str:
        #1) Confirm required inputs
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
            payload = {"error": f"Missing required field(s): {', '.join(missing)}"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        #2) Retrieve DB
        events: list[dict[str, Any]] = data.get("game_day_events", [])

        #4) Establish a new event row
        new_event = {
            "event_id": get_next_event_id(data),
            "game_pk": game_pk,
            "pitch_id": pitch_id,
            "timestamp_utc": get_current_timestamp(),  #May be populated later if necessary
            "leverage_index": leverage_index,
            "is_manual_alert": is_manual_alert,
            "suggestion_text": suggestion_text,
            "draft_status": "draft",
        }

        #5) Add to DB
        events.append(new_event)
        payload = new_event
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "createGameDayEvent",
                "description": (
                    "Create a new game-day event. event_id is generated automatically "
                    "(max existing + 1). draft_status defaults to 'Draft'."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "game_pk": {
                            "type": "integer",
                            "description": "Game primary key this event belongs to.",
                        },
                        "pitch_id": {
                            "type": "integer",
                            "description": "Pitch ID associated with the event.",
                        },
                        "leverage_index": {
                            "type": "number",
                            "description": "Leverage index for the event.",
                        },
                        "is_manual_alert": {
                            "type": "boolean",
                            "description": "True if the alert is manually triggered, else False.",
                        },
                        "suggestion_text": {
                            "type": "string",
                            "description": "Suggestion text for the event.",
                        },
                    },
                    "required": [
                        "game_pk",
                        "leverage_index",
                        "is_manual_alert",
                        "suggestion_text",
                    ],
                },
            },
        }
