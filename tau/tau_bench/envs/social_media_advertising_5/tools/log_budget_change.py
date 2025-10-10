# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class LogBudgetChange(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], adset_id, changed_at, new_budget, old_budget, reason) -> str:
        rows = list(data.get("budget_changes", {}).values())
        nid = f"BC-{max((int(r['change_id'][3:]) for r in rows), default=0) + 1}"
        rec = {"change_id": nid, "adset_id": adset_id, "old_budget": old_budget,
               "new_budget": new_budget, "changed_at": changed_at,
               "reason": reason}
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
