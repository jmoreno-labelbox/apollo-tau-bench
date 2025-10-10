# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _fixed_now_iso


class ModifyAccessCheck(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        updates = kwargs.get("updates") or {}
        check_id = kwargs.get("check_id")
        checks = list(data.get("access_checks", {}).values())
        for c in checks:
            if c.get("check_id") == check_id:
                c.update(updates)
                c["updated_at"] = _fixed_now_iso()
        return json.dumps({"updated_check_id": check_id, "updates": updates}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"update_access_check",
            "description":"Update an access check status.",
            "parameters":{"type":"object","properties":{"check_id":{"type":"string"},"updates":{"type":"object"}},"required":["check_id","updates"]}
        }}
