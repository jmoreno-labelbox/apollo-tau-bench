# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class LogStrategyChange(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        rows = data.get("strategy_changes", [])
        nid = f"SC-{max((int(r['change_id'][3:]) for r in rows), default=0) + 1}"
        rec = {"change_id": nid, "adset_id": kwargs.get("adset_id"), "old_strategy": kwargs.get("old_strategy"),
               "new_strategy": kwargs.get("new_strategy"), "old_bid": kwargs.get("old_bid"),
               "new_bid": kwargs.get("new_bid"), "changed_at": kwargs.get("changed_at"), "reason": kwargs.get("reason")}
        rows.append(rec)
        data["strategy_changes"] = rows
        return json.dumps(rec)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function",
                "function": {"name": "log_strategy_change", "description": "Appends a strategy change log entry.",
                             "parameters": {"type": "object", "properties": {"adset_id": {"type": "string"},
                                                                             "old_strategy": {"type": "string"},
                                                                             "new_strategy": {"type": "string"},
                                                                             "old_bid": {"type": ["number", "null"]},
                                                                             "new_bid": {"type": ["number", "null"]},
                                                                             "changed_at": {"type": "string"},
                                                                             "reason": {"type": "string"}},
                                            "required": ["adset_id", "old_strategy", "new_strategy", "old_bid",
                                                         "new_bid", "changed_at", "reason"]}}}
