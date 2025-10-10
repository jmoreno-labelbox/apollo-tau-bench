# Copyright © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class RemoveAccessCheck(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        check_id = kwargs.get("check_id")
        checks = list(data.get("access_checks", {}).values())
        data["access_checks"] = [c for c in checks if c.get("check_id") != check_id]
        return json.dumps({"removed_check_id": check_id}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"remove_access_check",
            "description":"Remove an access check by ID.",
            "parameters":{"type":"object","properties":{"check_id":{"type":"string"}},"required":["check_id"]}
        }}
