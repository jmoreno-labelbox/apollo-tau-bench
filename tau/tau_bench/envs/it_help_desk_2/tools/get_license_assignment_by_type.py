from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetLicenseAssignmentByType(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], employee_id: str = None, license_type: str = None) -> str:
        assignments = data.get("license_assignments", [])
        assignment = next(
            (
                a
                for a in assignments
                if a.get("employee_id") == employee_id
                and a.get("license_id") == license_type
                and a.get("status") == "active"
            ),
            None,
        )
        if not assignment:
            payload = {
                "error": f"Active assignment for license {license_type} not found for employee {employee_id}."
            }
            out = json.dumps(payload, indent=2)
            return out
        payload = assignment
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getLicenseAssignmentByType",
                "description": "Get a specific active license assignment for a user by license ID.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "employee_id": {"type": "string"},
                        "license_type": {"type": "string"},
                    },
                    "required": ["employee_id", "license_type"],
                },
            },
        }
