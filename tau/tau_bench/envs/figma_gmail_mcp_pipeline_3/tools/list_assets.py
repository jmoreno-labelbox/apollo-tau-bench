# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class list_assets(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        rows = list(_ensure(data, "assets", []))
        return _ok({"rows": rows})

    @staticmethod
    def get_info()->Dict[str,Any]:
        return {"type":"function","function":{
            "name":"list_assets",
            "description":"List exported assets and reports.",
            "parameters":{"type":"object","properties":{}}
        }}
