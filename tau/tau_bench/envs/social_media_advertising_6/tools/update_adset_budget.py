from tau_bench.envs.tool import Tool
import copy
import json
from typing import Any

class UpdateAdsetBudget(Tool):
    """Modify daily_budget with specified timestamp & request_id; records in budget_changes."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        adset_id: str,
        new_budget: float,
        timestamp: str,
        request_id: str,
        reason: str = "manual"
    ) -> str:
        req = ["adset_id", "new_budget", "timestamp", "request_id"]
        err = _require(locals(), req)
        if err:
            return _fail(err)
        adsets = _assert_table(data, "adsets")
        row = next(
            (r for r in adsets if str(r.get("adset_id")) == str(adset_id)),
            None,
        )
        if not row:
            return _fail("adset_not_found")
        old = float(row.get("daily_budget", 0.0))
        new = float(new_budget)
        if new != old:
            row["daily_budget"] = new
            row["updated_at"] = timestamp
            _assert_table(data, "budget_changes").append(
                {
                    "adset_id": str(adset_id),
                    "old_budget": old,
                    "new_budget": new,
                    "changed_at": timestamp,
                    "reason": reason,
                    "request_id": request_id,
                }
            )
        payload = {
            "ok": True,
            "adset_id": str(adset_id),
            "old_budget": old,
            "new_budget": new,
        }
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "updateAdsetBudget",
                "description": "Write a budget change and log it.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "adset_id": {"type": "string"},
                        "new_budget": {"type": "number"},
                        "timestamp": {"type": "string"},
                        "request_id": {"type": "string"},
                        "reason": {"type": "string"},
                    },
                    "required": ["adset_id", "new_budget", "timestamp", "request_id"],
                },
            },
        }
