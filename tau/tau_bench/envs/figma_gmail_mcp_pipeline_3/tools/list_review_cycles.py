# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


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
