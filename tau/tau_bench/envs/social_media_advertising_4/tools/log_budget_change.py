# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class LogBudgetChange(Tool):
    """Adds an entry to the budget change log."""
    @staticmethod
    def invoke(data: Dict[str, Any], adset_id, new_budget, old_budget, reason) -> str:
        changes = data.get('budget_changes', [])
        new_id = f"BC-{max((int(c['change_id'][3:]) for c in changes), default=0) + 1}"
        new_log = {"change_id": new_id, "adset_id": adset_id, "old_budget": old_budget, "new_budget": new_budget, "changed_at": "2025-08-15T01:00:00Z", "reason": reason}
        changes.append(new_log)
        data['budget_changes'] = changes
        return json.dumps(new_log)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "log_budget_change", "description": "Writes an audit log entry for an ad set budget change.", "parameters": {"type": "object", "properties": {"adset_id": {"type": "string"}, "old_budget": {"type": "number"}, "new_budget": {"type": "number"}, "reason": {"type": "string"}}, "required": ["adset_id", "old_budget", "new_budget", "reason"]}}}
