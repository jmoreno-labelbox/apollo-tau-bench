from tau_bench.envs.tool import Tool
import ast
import json
from datetime import datetime
from typing import Any

class LogBudgetChange(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any], 
        adset_id: str = None, 
        old_budget: float = None, 
        new_budget: float = None, 
        changed_at: str = None, 
        reason: str = None
    ) -> str:
        rows = data.get("budget_changes", [])
        nid = f"BC-{max((int(r['change_id'][3:]) for r in rows), default=0) + 1}"
        rec = {
            "change_id": nid,
            "adset_id": adset_id,
            "old_budget": old_budget,
            "new_budget": new_budget,
            "changed_at": changed_at,
            "reason": reason,
        }
        rows.append(rec)
        data["budget_changes"] = rows
        payload = rec
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "LogBudgetChange",
                "description": "Appends a budget change log entry.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "adset_id": {"type": "string"},
                        "old_budget": {"type": "number"},
                        "new_budget": {"type": "number"},
                        "changed_at": {"type": "string"},
                        "reason": {"type": "string"},
                    },
                    "required": [
                        "adset_id",
                        "old_budget",
                        "new_budget",
                        "changed_at",
                        "reason",
                    ],
                },
            },
        }
