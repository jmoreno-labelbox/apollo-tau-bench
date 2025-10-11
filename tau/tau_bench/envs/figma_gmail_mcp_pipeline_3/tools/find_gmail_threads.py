# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _params
def _j(v):
    return v if isinstance(v, str) else json.dumps(v, separators=(",", ":"), ensure_ascii=False)

def _params(data: Dict[str, Any], kwargs: Dict[str, Any]) -> Dict[str, Any]:
    return kwargs or {}

def _ok(x):
    return _j(x)

def _ensure(data: Dict[str, Any], key: str, default):
    if key not in data or data[key] is None:
        data[key] = default
    return data[key]

class find_gmail_threads(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], ) -> str:
        p = _params(data, kwargs)
        rows = []
        threads = _ensure(data, "gmail_threads", [])
        label_q = p.get("label_contains")
        subj_q = p.get("subject_contains")
        party_q = p.get("participant_email")

        for t in threads:
            ok = True
            if label_q:
                labels = t.get("labels", [])
                ok &= any(label_q.lower() in (lab or "").lower() for lab in labels)
            if subj_q:
                ok &= subj_q.lower() in (t.get("subject","").lower())
            if party_q:
                parts = set(t.get("participants", []))
                ok &= party_q in parts
            if ok:
                rows.append({
                    "thread_id": t.get("thread_id"),
                    "subject": t.get("subject"),
                    "participants": t.get("participants", []),
                    "current_labels": t.get("labels", []),
                })
        return _ok({"rows": rows})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"find_gmail_threads",
            "description":"Search Gmail threads by label, subject, or participant.",
            "parameters":{"type":"object","properties":{
                "label_contains":{"type":"string"},
                "subject_contains":{"type":"string"},
                "participant_email":{"type":"string"},
            }}
        }}