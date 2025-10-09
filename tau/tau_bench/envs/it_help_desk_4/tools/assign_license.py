from tau_bench.envs.tool import Tool
import json
from typing import Any

class AssignLicense(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], account_id: str = None, employee_id: str = None, license_id: str = None) -> str:
        assignments = data.setdefault("license_assignments", [])
        assignment_id = _get_next_id(assignments, "assignment_id", "lca")
        new_assignment = {
            "assignment_id": assignment_id,
            "account_id": account_id,
            "employee_id": employee_id,
            "license_id": license_id,
            "status": "active",
            "assigned_at": FIXED_NOW,
        }
        assignments.append(new_assignment)
        payload = new_assignment
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AssignLicense",
                "description": "Assign a single license to a user by creating an assignment record. Does not check availability.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "account_id": {"type": "string"},
                        "employee_id": {"type": "string"},
                        "license_id": {"type": "string"},
                    },
                    "required": ["account_id", "employee_id", "license_id"],
                },
            },
        }
