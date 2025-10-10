# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class LogBudgetChange(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        rows = data.get("budget_changes", [])
        nid = f"BC-{max((int(r['change_id'][3:]) for r in rows), default=0) + 1}"
        rec = {"change_id": nid, "adset_id": kwargs.get("adset_id"), "old_budget": kwargs.get("old_budget"),
               "new_budget": kwargs.get("new_budget"), "changed_at": kwargs.get("changed_at"),
               "reason": kwargs.get("reason")}
        rows.append(rec)
        data["budget_changes"] = rows
        return json.dumps(rec)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function",
                "function": {"name": "log_budget_change", "description": "Appends a budget change log entry.",
                             "parameters": {"type": "object", "properties": {"adset_id": {"type": "string"},
                                                                             "old_budget": {"type": "number"},
                                                                             "new_budget": {"type": "number"},
                                                                             "changed_at": {"type": "string"},
                                                                             "reason": {"type": "string"}},
                                            "required": ["adset_id", "old_budget", "new_budget", "changed_at",
                                                         "reason"]}}}
