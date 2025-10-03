from tau_bench.envs.tool import Tool
import json
import re
from typing import Any

class ListGameDayEvents(Tool):
    """Retrieves events for a game with optional filters. Note: min_leverage serves as a general ≥ filter; 'high leverage' according to policy applies strict > 1.5."""
    @staticmethod
    def invoke(data, game_pk: int, min_leverage: float = None, is_manual_alert: bool = None, draft_status: str = None) -> str:
        err = _require_tables(data, ["game_day_events"])
        if err:
            payload = {"error": err}
            out = json.dumps(payload, indent=2)
            return out
        if game_pk is None:
            payload = {"error": "game_pk is required."}
            out = json.dumps(payload, indent=2)
            return out
        rows = [e for e in data["game_day_events"] if e.get("game_pk") == game_pk]
        if min_leverage is not None:
            rows = [e for e in rows if (e.get("leverage_index") or 0) >= float(min_leverage)]
        if is_manual_alert is not None:
            rows = [
                e for e in rows if bool(e.get("is_manual_alert")) == bool(is_manual_alert)
            ]
        if draft_status:
            rows = [e for e in rows if e.get("draft_status") == draft_status]
        payload = rows
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "ListGameDayEvents",
                "description": "Lists game_day_events for a game with optional filters.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "game_pk": {"type": "integer"},
                        "min_leverage": {"type": "number"},
                        "is_manual_alert": {"type": "boolean"},
                        "draft_status": {"type": "string"},
                    },
                    "required": ["game_pk"],
                },
            },
        }
