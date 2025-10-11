# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool






def _small_fields(row: Dict[str, Any], fields: List[str]) -> Dict[str, Any]:
    """Return selected fields only (simple outputs)."""
    return {k: row.get(k) for k in fields}

def _require_str(arg: Any, name: str) -> Optional[str]:
    """Return arg as str if valid, else None."""
    return arg if isinstance(arg, str) and arg.strip() else None

class GetThreadMessagesTool(Tool):
    """Return simple message info (sender, ts, snippet) for a thread."""

    @staticmethod
    def invoke(data: Dict[str, Any], thread_id) -> str:
        thread_id = _require_str(thread_id, "thread_id")
        if not thread_id:
            return json.dumps({"error":"thread_id is required"})

        msgs = list(data.get("gmail_messages", {}).values())
        out = []
        for m in msgs:
            if m.get("thread_id") == thread_id:
                out.append(_small_fields(m, ["message_id","from_email","created_ts","snippet"]))
        out.sort(key=lambda r: r.get("created_ts",""))
        return json.dumps(out, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"get_thread_messages",
            "description":"List messages for a thread (sender, ts, snippet only).",
            "parameters":{"type":"object","properties":{
                "thread_id":{"type":"string"}
            },"required":["thread_id"]}
        }}