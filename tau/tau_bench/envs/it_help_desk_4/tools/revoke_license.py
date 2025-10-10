# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class RevokeLicense(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], assignment_id) -> str:
        assignments = list(data.get("license_assignments", {}).values())
        assignment = next((a for a in assignments if a.get("assignment_id") == assignment_id), None)
        if not assignment:
            return json.dumps({"error": f"Assignment {assignment_id} not found."}, indent=2)
        assignment["status"] = "revoked"
        assignment["revoked_at"] = FIXED_NOW
        return json.dumps(assignment, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "revoke_license", "description": "Revoke a user's license by updating its status. Does not check inventory.", "parameters": {"type": "object", "properties": {"assignment_id": {"type": "string"}}, "required": ["assignment_id"]}}}
