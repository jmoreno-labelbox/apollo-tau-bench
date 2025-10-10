# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class SyncGmailIntentsToReviewTool(Tool):
    """Scan thread messages for intent keywords and update review status counts (no status change)."""

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        cycle_id = _require_str(kwargs.get("cycle_id"), "cycle_id")
        thread_id = _require_str(kwargs.get("thread_id"), "thread_id")
        if not (cycle_id and thread_id):
            return json.dumps({"error":"cycle_id and thread_id required"})

        intents = _get_config_json(data, "intent_keywords")
        approve = [s.lower() for s in intents.get("approve", [])]
        changes = [s.lower() for s in intents.get("changes", [])]
        blocker = [s.lower() for s in intents.get("blocker", [])]

        msgs = data.get("gmail_messages", [])
        counts = {"approve":0, "changes":0, "blocker":0}
        for m in msgs:
            if m.get("thread_id") != thread_id:
                continue
            body = (m.get("body") or "").lower()
            if any(k in body for k in approve):
                counts["approve"] += 1
            if any(k in body for k in changes):
                counts["changes"] += 1
            if any(k in body for k in blocker):
                counts["blocker"] += 1

        # Store counts on cycle for visibility (non-destructive)
        cycles = _safe_table(data, "review_cycles")
        idx = _index_by(cycles, "cycle_id")
        if cycle_id in idx:
            c = cycles[idx[cycle_id]]
            c["intent_counts"] = counts

        return json.dumps({"cycle_id": cycle_id, "thread_id": thread_id, "intent_counts": counts}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"sync_gmail_intents_to_review",
            "description":"Parse thread for intent keywords (config-driven) and store counts on the cycle (no status change).",
            "parameters":{"type":"object","properties":{
                "cycle_id":{"type":"string"},
                "thread_id":{"type":"string"}
            },"required":["cycle_id","thread_id"]}
        }}
