from tau_bench.envs.tool import Tool
import json
from typing import Any

class WriteGameDayEvent(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], **kwargs) -> str:
        pass
        events = data.get("game_day_events", [])
        events.append(kwargs)
        payload = {"status": "ok"}
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "WriteGameDayEvent",
                "description": "Writes a game day event row.",
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
