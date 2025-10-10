# Sierra Copyright

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class LogStrategyChange(Tool):
    """Adds a new entry to the strategy_changes table."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        adset_id = kwargs.get("adset_id")
        old_strategy = kwargs.get("old_strategy")
        new_strategy = kwargs.get("new_strategy")
        old_bid = kwargs.get("old_bid")
        new_bid = kwargs.get("new_bid")
        changed_at = kwargs.get("changed_at")
        reason = kwargs.get("reason")
        
        if not adset_id:
            return json.dumps({"error": "adset_id is a required parameter."})
        if not old_strategy:
            return json.dumps({"error": "old_strategy is a required parameter."})
        if not new_strategy:
            return json.dumps({"error": "new_strategy is a required parameter."})
        if not changed_at:
            return json.dumps({"error": "changed_at is a required parameter."})
        if not reason:
            return json.dumps({"error": "reason is a required parameter."})

        new_strategy_change = {
            "change_id": f"SC-{adset_id}",
            "adset_id": adset_id,
            "old_strategy": old_strategy,
            "new_strategy": new_strategy,
            "old_bid": old_bid,
            "new_bid": new_bid,
            "changed_at": changed_at,
            "reason": reason
        }
        
        if "strategy_changes" not in data:
            data["strategy_changes"] = []
            
        data['strategy_changes'].append(new_strategy_change)

        return json.dumps(
            {
                "status": "success",
                "message": f"New strategy change was added: {new_strategy_change}",
            }
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "log_strategy_change",
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
                        }
                    },
                    "required": ["adset_id", "old_strategy", "new_strategy", "changed_at", "reason"],
                },
            },
        }
