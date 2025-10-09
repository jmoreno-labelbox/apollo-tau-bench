from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any

class LogBudgetChange(Tool):
    """Records an entry in the budget change log."""

    @staticmethod
    def invoke(data: dict[str, Any], adset_id: str = None, old_budget: float = None, new_budget: float = None, reason: str = None) -> str:
        changes = data.get("budget_changes", [])
        new_id = f"BC-{max((int(c['change_id'][3:]) for c in changes), default=0) + 1}"
        new_log = {
            "change_id": new_id,
            "adset_id": adset_id,
            "old_budget": old_budget,
            "new_budget": new_budget,
            "changed_at": "2025-08-15T01:00:00Z",
            "reason": reason,
        }
        changes.append(new_log)
        data["budget_changes"] = changes
        payload = new_log
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "LogBudgetChange",
                "description": "Writes an audit log entry for an ad set budget change.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "adset_id": {"type": "string"},
                        "old_budget": {"type": "number"},
                        "new_budget": {"type": "number"},
                        "reason": {"type": "string"},
                    },
                    "required": ["adset_id", "old_budget", "new_budget", "reason"],
                },
            },
        }
