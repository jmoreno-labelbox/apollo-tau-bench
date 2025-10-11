# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _params, _require


class list_gmail_messages(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        p = _params(data, kwargs)
        miss = _require(p, ["thread_id"])
        if miss: return miss
        rows = []
        messages = _ensure(data, "gmail_messages", [])
        for m in messages:
            if m.get("thread_id") == p["thread_id"]:
                rows.append({
                    "message_id": m.get("message_id"),
                    "sender_email": m.get("sender_email"),
                    "recipients": m.get("recipients", []),
                    "body_html": m.get("body_html"),
                    "timestamp": m.get("timestamp"),
                })
                break
        return _ok({"rows": rows})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"list_gmail_messages",
            "description":"List messages for a Gmail thread.",
            "parameters":{"type":"object","properties":{
                "thread_id":{"type":"string"}
            }}
        }}
