# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class LogStrategyChange(Tool):
    """Adds an entry to the bid strategy change log."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        changes = data.get('strategy_changes', [])
        new_id = f"SC-{max((int(c['change_id'][3:]) for c in changes), default=0) + 1}"
        new_log = {"change_id": new_id, "adset_id": kwargs.get("adset_id"), "old_strategy": kwargs.get("old_strategy"), "new_strategy": kwargs.get("new_strategy"), "old_bid": kwargs.get("old_bid"), "new_bid": kwargs.get("new_bid"), "changed_at": "2025-08-15T02:00:00Z", "reason": kwargs.get("reason")}
        changes.append(new_log)
        data['strategy_changes'] = changes
        return json.dumps(new_log)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "log_strategy_change", "description": "Writes an audit log entry for an ad set bid strategy change.", "parameters": {"type": "object", "properties": {"adset_id": {"type": "string"}, "old_strategy": {"type": "string"}, "new_strategy": {"type": "string"}, "old_bid": {"type": "number"}, "new_bid": {"type": "number"}, "reason": {"type": "string"}}, "required": ["adset_id", "old_strategy", "new_strategy", "old_bid", "new_bid", "reason"]}}}
