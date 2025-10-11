# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class AddAccessCheck(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], check) -> str:
        new_check = check or {}
        checks = list(data.get("access_checks", {}).values())
        checks.append(new_check)
        data["access_checks"] = checks
        return json.dumps({"added_check": new_check}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type":"function","function":{
            "name":"add_access_check",
            "description":"Add a new access check.",
            "parameters":{"type":"object","properties":{"check":{"type":"object"}},"required":["check"]}
        }}
