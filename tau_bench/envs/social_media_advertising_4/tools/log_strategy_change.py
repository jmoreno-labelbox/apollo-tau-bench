from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any

class LogStrategyChange(Tool):
    """Records an entry in the bid strategy change log."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        adset_id: str = None,
        old_strategy: str = None,
        new_strategy: str = None,
        old_bid: float = None,
        new_bid: float = None,
        reason: str = None
,
    change_id: Any = None,
    ) -> str:
        changes = data.get("strategy_changes", [])
        new_id = f"SC-{max((int(c['change_id'][3:]) for c in changes), default=0) + 1}"
        new_log = {
            "change_id": new_id,
            "adset_id": adset_id,
            "old_strategy": old_strategy,
            "new_strategy": new_strategy,
            "old_bid": old_bid,
            "new_bid": new_bid,
            "changed_at": "2025-08-15T02:00:00Z",
            "reason": reason,
        }
        changes.append(new_log)
        data["strategy_changes"] = changes
        payload = new_log
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "LogStrategyChange",
                "description": "Writes an audit log entry for an ad set bid strategy change.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "adset_id": {"type": "string"},
                        "old_strategy": {"type": "string"},
                        "new_strategy": {"type": "string"},
                        "old_bid": {"type": "number"},
                        "new_bid": {"type": "number"},
                        "reason": {"type": "string"},
                    },
                    "required": [
                        "adset_id",
                        "old_strategy",
                        "new_strategy",
                        "old_bid",
                        "new_bid",
                        "reason",
                    ],
                },
            },
        }
