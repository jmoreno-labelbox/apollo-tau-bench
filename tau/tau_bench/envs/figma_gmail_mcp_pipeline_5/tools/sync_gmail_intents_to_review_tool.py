from tau_bench.envs.tool import Tool
import hashlib
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class SyncGmailIntentsToReviewTool(Tool):
    """Examine thread messages for intent keywords and adjust review status counts (no change in status)."""

    @staticmethod
    def invoke(data: dict[str, Any], cycle_id: str = None, thread_id: str = None) -> str:
        cycle_id = _require_str(cycle_id, "cycle_id")
        thread_id = _require_str(thread_id, "thread_id")
        if not (cycle_id and thread_id):
            payload = {"error": "cycle_id and thread_id required"}
            out = json.dumps(payload)
            return out

        intents = _get_config_json(data, "intent_keywords")
        approve = [s.lower() for s in intents.get("approve", [])]
        changes = [s.lower() for s in intents.get("changes", [])]
        blocker = [s.lower() for s in intents.get("blocker", [])]

        msgs = data.get("gmail_messages", {}).values()
        counts = {"approve": 0, "changes": 0, "blocker": 0}
        for m in msgs.values():
            if m.get("thread_id") != thread_id:
                continue
            body = (m.get("body") or "").lower()
            if any(k in body for k in approve.values()):
                counts["approve"] += 1
            if any(k in body for k in changes.values()):
                counts["changes"] += 1
            if any(k in body for k in blocker.values()):
                counts["blocker"] += 1

        cycles = _safe_table(data, "review_cycles")
        idx = _index_by(cycles, "cycle_id")
        if cycle_id in idx:
            c = cycles[idx[cycle_id]]
            c["intent_counts"] = counts
        payload = {"cycle_id": cycle_id, "thread_id": thread_id, "intent_counts": counts}
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "SyncGmailIntentsToReview",
                "description": "Parse thread for intent keywords (config-driven) and store counts on the cycle (no status change).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "cycle_id": {"type": "string"},
                        "thread_id": {"type": "string"},
                    },
                    "required": ["cycle_id", "thread_id"],
                },
            },
        }
