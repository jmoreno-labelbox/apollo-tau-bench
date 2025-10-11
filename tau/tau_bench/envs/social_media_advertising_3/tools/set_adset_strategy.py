# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class SetAdsetStrategy(Tool):
    @staticmethod
    def invoke(data, adset_id, bid_amount, bid_strategy, new_budget, reason) -> str:
        """
        Set an ad set's bidding strategy and (when applicable) bid amount. Must include an audit reason.
        Required: adset_id (str), bid_strategy ('cost_cap'|'lowest_cost'|'bid_cap'), reason (str)
        Optional: bid_amount (float when 'cost_cap' or 'bid_cap'), new_budget (float)
        Side effects:
          - Mutates bid_strategy/bid_amount
          - If new_budget provided, writes BOTH 'budget' and 'daily_budget'
          - Appends an entry to data['strategy_changes']
        """
        import json, time

        adset_id = str(adset_id)

        if bid_strategy in ("cost_cap", "bid_cap") and bid_amount is None:
            return json.dumps({"ok": False, "error": "bid_amount is required for cost_cap or bid_cap"}, indent=2)

        adsets = data.get("adsets", [])
        target = next((a for a in adsets if str(a.get("adset_id") or a.get("id")) == adset_id), None)
        if target is None:
            return json.dumps({"ok": False, "error": f"adset '{adset_id}' not found"}, indent=2)

        if new_budget is not None:
            try:
                nb = float(new_budget)
            except Exception:
                return json.dumps({"ok": False, "error": "new_budget must be a number"}, indent=2)
            target["budget"] = nb
            target["daily_budget"] = nb

        target["bid_strategy"] = bid_strategy
        applied_bid = None
        if bid_strategy == "lowest_cost":
            target.pop("bid_amount", None)
        else:
            try:
                applied_bid = float(bid_amount)
            except Exception:
                return json.dumps({"ok": False, "error": "bid_amount must be a number"}, indent=2)
            target["bid_amount"] = applied_bid

        strategy_changes = data.setdefault("strategy_changes", [])
        strategy_changes.append({
            "adset_id": adset_id,
            "bid_strategy": bid_strategy,
            "bid_amount": applied_bid,
            "new_budget": float(new_budget) if new_budget is not None else None,
            "reason": reason,
            "ts": int(time.time())
        })

        return json.dumps({
            "ok": True,
            "adset_id": adset_id,
            "bid_strategy": bid_strategy,
            "bid_amount": applied_bid,
            "budget": target.get("budget"),
            "daily_budget": target.get("daily_budget"),
            "reason": reason
        }, indent=2)

    @staticmethod
    def get_info():
        return {
            "type": "function",
            "function": {
                "name": "set_adset_strategy",
                "description": "Set bidding strategy (and bid) for an ad set with an auditable reason. If new_budget is provided, writes both 'budget' and 'daily_budget'.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "adset_id": {"type": "string"},
                        "bid_strategy": {"type": "string", "enum": ["cost_cap", "lowest_cost", "bid_cap"]},
                        "bid_amount": {"type": ["number", "null"]},
                        "new_budget": {"type": ["number", "null"]},
                        "reason": {"type": "string"}
                    },
                    "required": ["adset_id", "bid_strategy", "reason"]
                }
            }
        }
