# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _params, _require


class create_gmail_thread(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        p = _params(data, kwargs)
        miss = _require(p, ["subject","sender_email","recipients","request_id"])
        if miss: return miss
        threads = _ensure(data, "gmail_threads", [])
        thread_id = f"thr_{p['request_id']}"
        thread = {
            "thread_id": thread_id,
            "subject": p.get("subject",""),
            "participants": list({p["sender_email"], *p.get("recipients",[])}),
            "labels": [],
            "messages": []
        }
        threads.append(thread)
        return _ok({"thread_id": thread_id})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"create_gmail_thread",
            "description":"Create a new Gmail thread.",
            "parameters":{"type":"object","properties":{
                "subject":{"type":"string"},
                "sender_email":{"type":"string"},
                "recipients":{"type":"array","items":{"type":"string"}},
                "timestamp":{"type":"string"},
                "request_id":{"type":"string"}
            },"required":["subject","sender_email","recipients","request_id"]}
        }}
