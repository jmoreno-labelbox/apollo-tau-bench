# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
def _j(v):
    return v if isinstance(v, str) else json.dumps(v, separators=(",", ":"), ensure_ascii=False)

def _ok(x):
    return _j(x)

def _ensure(data: Dict[str, Any], key: str, default):
    if key not in data or data[key] is None:
        data[key] = default
    return data[key]

class list_assets(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], ) -> str:
        rows = list(_ensure(data, "assets", []))
        return _ok({"rows": rows})

    @staticmethod
    def get_info()->Dict[str,Any]:
        return {"type":"function","function":{
            "name":"list_assets",
            "description":"List exported assets and reports.",
            "parameters":{"type":"object","properties":{}}
        }}