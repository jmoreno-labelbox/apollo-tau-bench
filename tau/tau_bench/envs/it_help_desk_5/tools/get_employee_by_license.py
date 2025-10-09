from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetEmployeeByLicense(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], license_id: str = None, status: str = None) -> str:
        if license_id is None or status is None:
            payload = {
                    "status": "error",
                    "reason": "The license_id and status fields are required.",
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        license_assignments = data.get("license_assignments")

        assignment_data = []

        for license in license_assignments:
            if license["license_id"] == license_id and license["status"] == status:
                assignment_data.append(license["employee_id"])
        payload = assignment_data
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getEmployeeByLicense",
                "description": "Returns the employees with licenses and statuses that match status.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "license_id": {
                            "type": "string",
                            "description": "The license to filter by.",
                        },
                        "status": {
                            "type": "string",
                            "desctiption": "The status of the license to filter by.",
                        },
                    },
                    "required": ["license_id", "status"],
                },
            },
        }
