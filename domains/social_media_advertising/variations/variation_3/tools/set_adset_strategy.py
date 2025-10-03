from tau_bench.envs.tool import Tool
import csv
import json
import re
from datetime import datetime
from typing import Any

class SetAdsetStrategy(Tool):
    @staticmethod
    def invoke(data, adset_id: str, bid_strategy: str, reason: str, bid_amount: float = None, new_budget: float = None) -> str:
        """
        Define an ad set's bidding strategy and, if applicable, the bid amount. An audit reason is required.
        Required: adset_id (str), bid_strategy ('cost_cap'|'lowest_cost'|'bid_cap'), reason (str)
        Optional: bid_amount (float for 'cost_cap' or 'bid_cap'), new_budget (float)
        Side effects:
          - Alters bid_strategy/bid_amount
          - If new_budget is provided, updates BOTH 'budget' and 'daily_budget'
          - Adds an entry to data['strategy_changes']
        """
        pass
        import json
        import time

        if bid_strategy in ("cost_cap", "bid_cap") and bid_amount is None:
            payload = {
                    "ok": False,
                    "error": "bid_amount is required for cost_cap or bid_cap",
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out

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

        if new_budget is not None:
            try:
                nb = float(new_budget)
            except Exception:
                payload = {"ok": False, "error": "new_budget must be a number"}
                out = json.dumps(
                    payload, indent=2
                )
                return out
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
                payload = {"ok": False, "error": "bid_amount must be a number"}
                out = json.dumps(
                    payload, indent=2
                )
                return out
            target["bid_amount"] = applied_bid

        strategy_changes = data.setdefault("strategy_changes", [])
        strategy_changes.append(
            {
                "adset_id": adset_id,
                "bid_strategy": bid_strategy,
                "bid_amount": applied_bid,
                "new_budget": float(new_budget) if new_budget is not None else None,
                "reason": reason,
                "ts": int(time.time()),
            }
        )
        payload = {
                "ok": True,
                "adset_id": adset_id,
                "bid_strategy": bid_strategy,
                "bid_amount": applied_bid,
                "budget": target.get("budget"),
                "daily_budget": target.get("daily_budget"),
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
                "name": "SetAdsetStrategy",
                "description": "Set bidding strategy (and bid) for an ad set with an auditable reason. If new_budget is provided, writes both 'budget' and 'daily_budget'.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "adset_id": {"type": "string"},
                        "bid_strategy": {
                            "type": "string",
                            "enum": ["cost_cap", "lowest_cost", "bid_cap"],
                        },
                        "bid_amount": {"type": ["number", "null"]},
                        "new_budget": {"type": ["number", "null"]},
                        "reason": {"type": "string"},
                    },
                    "required": ["adset_id", "bid_strategy", "reason"],
                },
            },
        }
