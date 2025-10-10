# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class DlpScanThreadTool(Tool):
    """Scan a thread's messages for DLP block patterns from config; returns found patterns."""

    @staticmethod
    def invoke(data: Dict[str, Any], thread_id) -> str:
        thread_id = _require_str(thread_id, "thread_id")
        if not thread_id:
            return json.dumps({"error":"thread_id is required"})

        dlp = _get_config_json(data, "dlp_config")
        patterns = dlp.get("block_patterns", []) if isinstance(dlp, dict) else []
        messages = list(data.get("gmail_messages", {}).values())
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
