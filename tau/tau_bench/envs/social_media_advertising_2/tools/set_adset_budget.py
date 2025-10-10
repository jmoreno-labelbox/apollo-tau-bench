# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class SetAdsetBudget(Tool):
    @staticmethod
    def invoke(data, **kwargs) -> str:
        """
        Update an ad set's daily budget. Must include an audit reason.
        Required: adset_id (str), new_budget (float), reason (str)
        Side effects:
          - Mutates data['adsets'][...] budget and daily_budget (kept in sync)
          - Appends an entry to data['budget_changes']
        Returns: {"ok": true, "adset_id": "...", "new_budget": <float>, "reason": "..."}
        """
        import json, time

        adset_id = str(kwargs["adset_id"])
        new_budget = float(kwargs["new_budget"])
        reason = kwargs["reason"]

        adsets = list(data.get("adsets", {}).values())
        target = next((a for a in adsets if str(a.get("adset_id") or a.get("id")) == adset_id), None)
        if target is None:
            return json.dumps({"ok": False, "error": f"adset '{adset_id}' not found"}, indent=2)

        target["budget"] = new_budget
        target["daily_budget"] = new_budget

        budget_changes = data.setdefault("budget_changes", [])
        budget_changes.append({
            "adset_id": adset_id,
            "new_budget": new_budget,
            "reason": reason,
            "ts": int(time.time())
        })

        return json.dumps({"ok": True, "adset_id": adset_id, "new_budget": new_budget, "reason": reason}, indent=2)

    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "set_adset_budget",
                "description": "Update daily budget for an ad set with an auditable reason. Writes both 'budget' and 'daily_budget'.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "adset_id": {"type": "string"},
                        "new_budget": {"type": "number"},
                        "reason": {"type": "string"}
                    },
                    "required": ["adset_id", "new_budget", "reason"]
                }
            }
        }
