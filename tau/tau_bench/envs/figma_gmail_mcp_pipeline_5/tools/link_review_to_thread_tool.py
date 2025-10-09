from tau_bench.envs.tool import Tool
import hashlib
import json
from typing import Any

class LinkReviewToThreadTool(Tool):
    """Associate a review cycle with a Gmail thread (idempotent)."""

    @staticmethod
    def invoke(data: dict[str, Any], cycle_id: str = None, thread_id: str = None, changed_ts: str = None) -> str:
        cycle_id = _require_str(cycle_id, "cycle_id")
        thread_id = _require_str(thread_id, "thread_id")
        changed_ts = _require_str(changed_ts, "changed_ts")
        if not (cycle_id and thread_id and changed_ts):
            payload = {"error": "cycle_id, thread_id, changed_ts required"}
            out = json.dumps(payload)
            return out

        cycles = _safe_table(data, "review_cycles")
        idx = _index_by(cycles, "cycle_id")
        if cycle_id not in idx:
            payload = {"error": f"cycle_id {cycle_id} not found"}
            out = json.dumps(payload)
            return out

        cycles[idx[cycle_id]]["thread_id_nullable"] = thread_id
        cycles[idx[cycle_id]]["last_updated"] = changed_ts
        payload = {"success": True, "cycle_id": cycle_id, "thread_id": thread_id}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "LinkReviewToThread",
                "description": "Link review cycle to Gmail thread (idempotent).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "cycle_id": {"type": "string"},
                        "thread_id": {"type": "string"},
                        "changed_ts": {"type": "string"},
                    },
                    "required": ["cycle_id", "thread_id", "changed_ts"],
                },
            },
        }
