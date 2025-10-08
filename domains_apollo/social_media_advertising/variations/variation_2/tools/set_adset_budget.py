from tau_bench.envs.tool import Tool
import csv
import json
import re
from datetime import datetime
from typing import Any

class SetAdsetBudget(Tool):
    @staticmethod
    def invoke(data, adset_id: str, new_budget: float, reason: str) -> str:
        """
        Modify an ad set's daily budget. An audit reason is mandatory.
        Required: adset_id (str), new_budget (float), reason (str)
        Side effects:
          - Alters data['adsets'][...] budget and daily_budget (kept synchronized)
          - Adds an entry to data['budget_changes']
        Returns: {"ok": true, "adset_id": "...", "new_budget": <float>, "reason": "..."}
        """
        import json
        import time

        adset_id = str(adset_id)
        new_budget = float(new_budget)
        reason = reason

        adsets = data.get("adsets", [])
        target = next(
            (a for a in adsets if str(a.get("adset_id") or a.get("id")) == adset_id),
            None,
        )
        if target is None:
            payload = {"ok": False, "error": f"adset '{adset_id}' not found"}
            out = json.dumps(
                payload, indent=2
            )
            return out

        target["budget"] = new_budget
        target["daily_budget"] = new_budget

        budget_changes = data.setdefault("budget_changes", [])
        budget_changes.append(
            {
                "adset_id": adset_id,
                "new_budget": new_budget,
                "reason": reason,
                "ts": int(time.time()),
            }
        )
        payload = {
                "ok": True,
                "adset_id": adset_id,
                "new_budget": new_budget,
                "reason": reason,
            }
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "SetAdsetBudget",
                "description": "Update daily budget for an ad set with an auditable reason. Writes both 'budget' and 'daily_budget'.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "adset_id": {"type": "string"},
                        "new_budget": {"type": "number"},
                        "reason": {"type": "string"},
                    },
                    "required": ["adset_id", "new_budget", "reason"],
                },
            },
        }
