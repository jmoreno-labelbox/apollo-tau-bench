# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class DlpScanAndLabelThreadTool(Tool):
    """Scan a thread for DLP issues and apply a label if any issues found (idempotent)."""

    @staticmethod
    def invoke(data: Dict[str, Any], changed_ts, label_if_found, thread_id) -> str:
        thread_id = _require_str(thread_id, "thread_id")
        label_if_found = _require_str(label_if_found, "label_if_found") or "dlp-flag"
        changed_ts = _require_str(changed_ts, "changed_ts")
        if not (thread_id and label_if_found and changed_ts):
            return json.dumps({"error":"thread_id, label_if_found, changed_ts required"})

        # Utilize existing DLP scan.
        scan = json.loads(DlpScanThreadTool.invoke(data, thread_id=thread_id))
        found = scan.get("blocked_terms_found", [])
        if found:
            # assign label
            _ = UpdateThreadLabelsTool.invoke(data, thread_id=thread_id, add_labels=[label_if_found], remove_labels=[], changed_ts=changed_ts)
        return json.dumps({"thread_id": thread_id, "blocked_terms_found": found, "label_applied": bool(found)}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"dlp_scan_and_label_thread",
            "description":"If DLP violations found in thread, apply a chosen label.",
            "parameters":{"type":"object","properties":{
                "thread_id":{"type":"string"},
                "label_if_found":{"type":"string"},
                "changed_ts":{"type":"string"}
            },"required":["thread_id","label_if_found","changed_ts"]}
        }}
