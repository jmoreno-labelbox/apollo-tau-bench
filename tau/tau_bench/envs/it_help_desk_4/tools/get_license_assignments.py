# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetLicenseAssignments(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], employee_id: Optional[str] = None, account_id: Optional[str] = None) -> str:
        results: List[Dict[str, Any]] = []
        for a in data["license_assignments"]:
            if employee_id and a["employee_id"] != employee_id:
                continue
            if account_id and a["account_id"] != account_id:
                continue
            results.append(a)
        return json.dumps({"status": "ok", "assignments": results})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_license_assignments",
                "description": "List license assignments filtered by employee_id or account_id.",
                "parameters": {
                    "type": "object",
                    "properties": {"employee_id": {"type": "string"}, "account_id": {"type": "string"}},
                    "required": [],
                },
            },
        }
