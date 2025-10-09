from tau_bench.envs.tool import Tool
import hashlib
import json
from typing import Any

class DlpScanAndLabelThreadTool(Tool):
    """Examine a thread for DLP issues and assign a label if any issues are detected (idempotent)."""

    @staticmethod
    def invoke(data: dict[str, Any], thread_id: str = None, label_if_found: str = "dlp-flag", changed_ts: str = None) -> str:
        thread_id = _require_str(thread_id, "thread_id")
        label_if_found = _require_str(label_if_found, "label_if_found")
        changed_ts = _require_str(changed_ts, "changed_ts")
        if not (thread_id and label_if_found and changed_ts):
            payload = {"error": "thread_id, label_if_found, changed_ts required"}
            out = json.dumps(
                payload)
            return out

        scan = json.loads(DlpScanThreadTool.invoke(data, thread_id=thread_id))
        found = scan.get("blocked_terms_found", [])
        if found:
            _ = UpdateThreadLabelsTool.invoke(
                data,
                thread_id=thread_id,
                add_labels=[label_if_found],
                remove_labels=[],
                changed_ts=changed_ts,
            )
        payload = {
                "thread_id": thread_id,
                "blocked_terms_found": found,
                "label_applied": bool(found),
            }
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "DlpScanAndLabelThread",
                "description": "If DLP violations found in thread, apply a chosen label.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "thread_id": {"type": "string"},
                        "label_if_found": {"type": "string"},
                        "changed_ts": {"type": "string"},
                    },
                    "required": ["thread_id", "label_if_found", "changed_ts"],
                },
            },
        }
