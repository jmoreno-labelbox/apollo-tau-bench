# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetCrewMemberByEmployeeCode(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], employee_code: str) -> str:
        for c in data.get("crew_members", []):
            if c.get("employee_code") == employee_code:
                return _j(c)
        return _j({})

    @staticmethod
    def get_info()->Dict[str,Any]:
        return {"type":"function","function":{
            "name":"get_crew_member_by_employee_code",
            "description":"Return one crew member by employee_code.",
            "parameters":{"type":"object","properties":{"employee_code":{"type":"string"}},"required":["employee_code"]}
        }}
