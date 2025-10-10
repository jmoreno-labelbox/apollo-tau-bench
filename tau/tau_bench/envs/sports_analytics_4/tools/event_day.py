# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class EventDay(Tool):
    @staticmethod
        # main invoke function
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        events = data.get("game_day_events", [])
        events.append(kwargs)
        # return result
        return json.dumps({"status": "ok"}, indent=2)

    @staticmethod
        # info metadata
    def get_info() -> Dict[str, Any]:
        # return result
        return {"type": "function", "function": {"name": "makeEvent", "description": "Persists a game day event row.", "parameters": {"type": "object", "properties": {"game_pk": {"type": "string"}, "leverage_index": {"type": "number"}, "is_manual_alert": {"type": "boolean"}, "suggestion_text": {"type": "string"}}, "required": ["game_pk", "leverage_index", "is_manual_alert"]}}}
