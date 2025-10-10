# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetLicenseAssignmentByType(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        employee_id = kwargs.get("employee_id")
        license_type = kwargs.get("license_type")
        assignments = data.get("license_assignments", [])
        assignment = next((a for a in assignments if a.get("employee_id") == employee_id and a.get("license_id") == license_type and a.get("status") == "active"), None)
        if not assignment:
            return json.dumps({"error": f"Active assignment for license {license_type} not found for employee {employee_id}."}, indent=2)
        return json.dumps(assignment, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "get_license_assignment_by_type", "description": "Get a specific active license assignment for a user by license ID.", "parameters": {"type": "object", "properties": {"employee_id": {"type": "string"}, "license_type": {"type": "string"}}, "required": ["employee_id", "license_type"]}}}
