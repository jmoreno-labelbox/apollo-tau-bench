from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any

class LogStrategyChange(Tool):
    """Inserts a new record into the strategy_changes table."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        adset_id: str = None,
        old_strategy: str = None,
        new_strategy: str = None,
        old_bid: float = None,
        new_bid: float = None,
        changed_at: str = None,
        reason: str = None
,
    change_id: Any = None,
    ) -> str:
        if not adset_id:
            payload = {"error": "adset_id is a required parameter."}
            out = json.dumps(payload)
            return out
        if not old_strategy:
            payload = {"error": "old_strategy is a required parameter."}
            out = json.dumps(payload)
            return out
        if not new_strategy:
            payload = {"error": "new_strategy is a required parameter."}
            out = json.dumps(payload)
            return out
        if not changed_at:
            payload = {"error": "changed_at is a required parameter."}
            out = json.dumps(payload)
            return out
        if not reason:
            payload = {"error": "reason is a required parameter."}
            out = json.dumps(payload)
            return out

        new_strategy_change = {
            "change_id": f"SC-{adset_id}",
            "adset_id": adset_id,
            "old_strategy": old_strategy,
            "new_strategy": new_strategy,
            "old_bid": old_bid,
            "new_bid": new_bid,
            "changed_at": changed_at,
            "reason": reason,
        }

        if "strategy_changes" not in data:
            data["strategy_changes"] = []

        data["strategy_changes"].append(new_strategy_change)
        payload = {
            "status": "success",
            "message": f"New strategy change was added: {new_strategy_change}",
        }
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "LogStrategyChange",
                "description": "Adds a new entry to the strategy_changes table.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "adset_id": {
                            "type": "string",
                            "description": "The ID of the ad set.",
                        },
                        "old_strategy": {
                            "type": "string",
                            "description": "The old bid strategy.",
                        },
                        "new_strategy": {
                            "type": "string",
                            "description": "The new bid strategy.",
                        },
                        "old_bid": {
                            "type": "number",
                            "description": "The old bid amount.",
                        },
                        "new_bid": {
                            "type": "number",
                            "description": "The new bid amount.",
                        },
                        "changed_at": {
                            "type": "string",
                            "description": "The timestamp of the change (ISO format).",
                        },
                        "reason": {
                            "type": "string",
                            "description": "The reason for the strategy change.",
                        },
                    },
                    "required": [
                        "adset_id",
                        "old_strategy",
                        "new_strategy",
                        "changed_at",
                        "reason",
                    ],
                },
            },
        }
