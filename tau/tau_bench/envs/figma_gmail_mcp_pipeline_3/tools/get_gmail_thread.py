# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _params, _require


class get_gmail_thread(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        p = _params(data, kwargs)
        miss = _require(p, ["thread_id"])
        if miss: return miss
        threads = _ensure(data, "gmail_threads", [])
        for t in threads:
            if t.get("thread_id") == p["thread_id"]:
                return _ok({"thread_id": t["thread_id"], "current_labels": t.get("labels", [])})
        return _ok({"thread_id": p["thread_id"], "current_labels": []})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"get_gmail_thread",
            "description":"Fetch a Gmail thread metadata.",
            "parameters":{"type":"object","properties":{
                "thread_id":{"type":"string"}
            },"required":["thread_id"]}
        }}
