# Copyright Sierra
import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
def _require_str(arg: Any, name: str) -> Optional[str]:
    """Return arg as str if valid, else None."""
    return arg if isinstance(arg, str) and arg.strip() else None
class UpdateThreadLabelsTool(Tool):
    """Update Gmail thread labels deterministically (idempotent)."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        thread_id = _require_str(kwargs.get("thread_id"), "thread_id")
        add_labels = kwargs.get("add_labels", []) or []
        remove_labels = kwargs.get("remove_labels", []) or []
        changed_ts = _require_str(kwargs.get("changed_ts"), "changed_ts")
        if not (thread_id and changed_ts):
            return json.dumps({"error":"thread_id and changed_ts required"})
        threads = _safe_table(data, "gmail_threads")
        idx = _index_by(threads, "thread_id")
        if thread_id not in idx:
            return json.dumps({"error": f"thread_id {thread_id} not found"})
        row = threads[idx[thread_id]]
        labels: List[str] = list(row.get("current_labels", []))
        for lab in add_labels:
            if lab not in labels:
                labels.append(lab)
        for lab in remove_labels:
            if lab in labels:
                labels.remove(lab)
        row["current_labels"] = labels
        row["updated_ts"] = changed_ts
        return json.dumps({"success": True, "thread_id": thread_id, "labels": labels}, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"update_thread_labels",
            "description":"Add/remove labels on a Gmail thread (idempotent). Requires explicit 'changed_ts'.",
            "parameters":{"type":"object","properties":{
                "thread_id":{"type":"string"},
                "add_labels":{"type":"array","items":{"type":"string"}},
                "remove_labels":{"type":"array","items":{"type":"string"}},
                "changed_ts":{"type":"string"}
            },"required":["thread_id","changed_ts"]}
        }}
class DlpScanThreadTool(Tool):
    """Scan a thread's messages for DLP block patterns from config; returns found patterns."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        thread_id = _require_str(kwargs.get("thread_id"), "thread_id")
        if not thread_id:
            return json.dumps({"error":"thread_id is required"})
        dlp = _get_config_json(data, "dlp_config")
        patterns = dlp.get("block_patterns", []) if isinstance(dlp, dict) else []
        messages = data.get("gmail_messages", [])
        found: Set[str] = set()
        for m in messages:
            if m.get("thread_id") != thread_id:
                continue
            body = (m.get("body") or "").lower()
            for p in patterns:
                if isinstance(p, str) and p.lower() in body:
                    found.add(p)
        return json.dumps({"thread_id": thread_id, "blocked_terms_found": sorted(found)}, indent=2)
    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"dlp_scan_thread",
            "description":"Scan thread messages for DLP block patterns from system config.",
            "parameters":{"type":"object","properties":{
                "thread_id":{"type":"string"}
            },"required":["thread_id"]}
        }}
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