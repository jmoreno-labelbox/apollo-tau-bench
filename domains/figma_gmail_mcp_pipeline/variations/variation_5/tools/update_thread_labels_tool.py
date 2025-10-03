from tau_bench.envs.tool import Tool
import hashlib
import json
from typing import Any

class UpdateThreadLabelsTool(Tool):
    """Modify Gmail thread labels in a deterministic manner (idempotent)."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        add_labels: list[str] = None,
        changed_ts: str = None,
        remove_labels: list[str] = None,
        thread_id: str = None
    ) -> str:
        add_labels = add_labels or []
        remove_labels = remove_labels or []
        thread_id = _require_str(thread_id, "thread_id")
        changed_ts = _require_str(changed_ts, "changed_ts")
        if not (thread_id and changed_ts):
            payload = {"error": "thread_id and changed_ts required"}
            out = json.dumps(payload)
            return out

        threads = _safe_table(data, "gmail_threads")
        idx = _index_by(threads, "thread_id")
        if thread_id not in idx:
            payload = {"error": f"thread_id {thread_id} not found"}
            out = json.dumps(payload)
            return out

        row = threads[idx[thread_id]]
        labels: list[str] = list(row.get("current_labels", []))
        for lab in add_labels:
            if lab not in labels:
                labels.append(lab)
        for lab in remove_labels:
            if lab in labels:
                labels.remove(lab)
        row["current_labels"] = labels
        row["updated_ts"] = changed_ts
        payload = {"success": True, "thread_id": thread_id, "labels": labels}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateThreadLabels",
                "description": "Add/remove labels on a Gmail thread (idempotent). Requires explicit 'changed_ts'.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "thread_id": {"type": "string"},
                        "add_labels": {"type": "array", "items": {"type": "string"}},
                        "remove_labels": {"type": "array", "items": {"type": "string"}},
                        "changed_ts": {"type": "string"},
                    },
                    "required": ["thread_id", "changed_ts"],
                },
            },
        }
