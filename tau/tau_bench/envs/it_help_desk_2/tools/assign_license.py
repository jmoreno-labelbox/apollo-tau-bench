# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class AssignLicense(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], account_id, employee_id, license_id) -> str:
        assignments = data.setdefault("license_assignments", [])
        assignment_id = _get_next_id(assignments, "assignment_id", "lca")
        new_assignment = {"assignment_id": assignment_id, "account_id": account_id, "employee_id": employee_id, "license_id": license_id, "status": "active", "assigned_at": FIXED_NOW}
        assignments.append(new_assignment)
        return json.dumps(new_assignment, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "assign_license", "description": "Assign a single license to a user by creating an assignment record. Does not check availability.", "parameters": {"type": "object", "properties": {"account_id": {"type": "string"}, "employee_id": {"type": "string"}, "license_id": {"type": "string"}}, "required": ["account_id", "employee_id", "license_id"]}}}
