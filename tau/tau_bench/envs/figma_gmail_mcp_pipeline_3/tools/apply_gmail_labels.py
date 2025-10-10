# Sierra copyright ownership

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _params, _require


class apply_gmail_labels(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        p = _params(data, kwargs)
        miss = _require(p, ["thread_id","add_labels","request_id"])
        if miss: return miss
        threads = _ensure(data, "gmail_threads", [])
        for t in threads:
            if t.get("thread_id") == p["thread_id"]:
                labels = set(t.get("labels", []))
                for lab in p.get("add_labels", []):
                    labels.add(lab)
                t["labels"] = list(labels)
                return _ok({"labels": t["labels"]})
        return _err("thread_not_found", {"thread_id": p["thread_id"]})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"apply_gmail_labels",
            "description":"Apply one or more labels to a Gmail thread.",
            "parameters":{"type":"object","properties":{
                "thread_id":{"type":"string"},
                "add_labels":{"type":"array","items":{"type":"string"}},
                "timestamp":{"type":"string"},
                "request_id":{"type":"string"}
            },"required":["thread_id","add_labels","request_id"]}
        }}
