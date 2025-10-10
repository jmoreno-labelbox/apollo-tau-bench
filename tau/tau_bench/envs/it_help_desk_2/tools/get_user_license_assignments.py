# Sierra Copyright

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetUserLicenseAssignments(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], employee_id) -> str:
        assignments = data.get("license_assignments", [])
        user_licenses = [a for a in assignments if a.get("employee_id") == employee_id and a.get("status") == "active"]
        return json.dumps(user_licenses, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "get_user_license_assignments", "description": "Get a list of all active license assignments for a given employee.", "parameters": {"type": "object", "properties": {"employee_id": {"type": "string"}}, "required": ["employee_id"]}}}
