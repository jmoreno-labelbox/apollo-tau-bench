from tau_bench.envs.tool import Tool
import json
from typing import Any

class EventDay(Tool):
    @staticmethod
    #primary invocation function
    def invoke(data: dict[str, Any], event: dict[str, Any] = None, game_pk: Any = None, leverage_index: Any = None, is_manual_alert: Any = None, suggestion_text: str = None) -> str:
        events = data.get("game_day_events", [])
        # Support both event dict and individual parameters
        if event is not None:
            events.append(event)
        else:
            # Build event from individual parameters
            event_obj = {}
            if game_pk is not None:
                event_obj['game_pk'] = game_pk
            if leverage_index is not None:
                event_obj['leverage_index'] = leverage_index
            if is_manual_alert is not None:
                event_obj['is_manual_alert'] = is_manual_alert
            if suggestion_text is not None:
                event_obj['suggestion_text'] = suggestion_text
            events.append(event_obj)
        payload = {"status": "ok"}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    #metadata information
    def get_info() -> dict[str, Any]:
        pass
        #return result
        return {
            "type": "function",
            "function": {
                "name": "makeEvent",
                "description": "Persists a game day event row.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "game_pk": {"type": "string"},
                        "leverage_index": {"type": "number"},
                        "is_manual_alert": {"type": "boolean"},
                        "suggestion_text": {"type": "string"},
                    },
                    "required": ["game_pk", "leverage_index", "is_manual_alert"],
                },
            },
        }
