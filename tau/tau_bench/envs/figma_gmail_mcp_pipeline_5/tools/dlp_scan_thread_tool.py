# Copyright Sierra

from typing import Set
import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool






def _require_str(arg: Any, name: str) -> Optional[str]:
    """Return arg as str if valid, else None."""
    return arg if isinstance(arg, str) and arg.strip() else None

def _get_config_json(data: Dict[str, Any], key: str) -> Dict[str, Any]:
    """Read a config row from system_config and parse its JSON value."""
    rows = data.get("system_config", [])
    for r in rows:
        if r.get("config_key") == key:
            try:
                return json.loads(r.get("config_value_json") or "{}")
            except Exception:
                return {}
    return {}

class DlpScanThreadTool(Tool):
    """Scan a thread's messages for DLP block patterns from config; returns found patterns."""

    @staticmethod
    def invoke(data: Dict[str, Any], thread_id) -> str:
        thread_id = _require_str(thread_id, "thread_id")
        if not thread_id:
            return json.dumps({"error":"thread_id is required"})

        dlp = _get_config_json(data, "dlp_config")
        patterns = dlp.get("block_patterns", []) if isinstance(dlp, dict) else []
        messages = list(list(list(data.get("gmail_messages", {}).values())) if isinstance(data.get("gmail_messages"), dict) else data.get("gmail_messages", []))
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