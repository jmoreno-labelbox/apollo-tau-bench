# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class append_gmail_message(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        p = _params(data, kwargs)
        miss = _require(p, ["thread_id","sender_email","body_html","request_id"])
        if miss: return miss
        threads = _ensure(data, "gmail_threads", [])
        for t in threads:
            if t.get("thread_id") == p["thread_id"]:
                msg_id = f"msg_{p['request_id']}"
                msg = {
                    "message_id": msg_id,
                    "sender_email": p["sender_email"],
                    "recipients": p.get("recipients", []),
                    "body_html": p["body_html"],
                    "timestamp": p.get("timestamp"),
                }
                t.setdefault("gmail_messages", []).append(msg)
                new_parts = set(t.get("participants", []))
                new_parts.add(p["sender_email"])
                for r in p.get("recipients", []):
                    new_parts.add(r)
                t["participants"] = list(new_parts)
                return _ok({"message_id": msg_id})
        return _err("thread_not_found", {"thread_id": p["thread_id"]})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"append_gmail_message",
            "description":"Append a message to an existing Gmail thread.",
            "parameters":{"type":"object","properties":{
                "thread_id":{"type":"string"},
                "sender_email":{"type":"string"},
                "recipients":{"type":"array","items":{"type":"string"}},
                "body_html":{"type":"string"},
                "timestamp":{"type":"string"},
                "request_id":{"type":"string"}
            },"required":["thread_id","sender_email","body_html","request_id"]}
        }}
