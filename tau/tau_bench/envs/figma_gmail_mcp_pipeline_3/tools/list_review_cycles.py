# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool






def _ok(x):
    return _j(x)

def _ensure(data: Dict[str, Any], key: str, default):
    if key not in data or data[key] is None:
        data[key] = default
    return data[key]

class list_review_cycles(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs)->str:
        return _ok({"rows": list(_ensure(data, "review_cycles", []))})

    @staticmethod
    def get_info()->Dict[str,Any]:
        return {"type":"function","function":{
            "name":"list_review_cycles",
            "description":"List review cycles.",
            "parameters":{"type":"object","properties":{}}
        }}