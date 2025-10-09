from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class MissingLicenses(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], employee_id: str = None, job_title: str = None) -> str:
        if employee_id is None or job_title is None:
            payload = {
                "status": "error",
                "description": "The employee_id and job_title fields are required.",
            }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        employee_licenses = []
        license_assignments = data.get("license_assignments", {}).values()

        for assignment in license_assignments.values():
            if assignment["employee_id"] == employee_id:
                employee_licenses.append(assignment["license_id"])

        group_map = data.get("rbac_group_map")
        missing = []

        for group in group_map.values():
            if group["job_title"] == job_title:
                licenses = group["default_license_bundle"]
                for license in licenses:
                    if license not in employee_licenses:
                        missing.append(license)
                payload = missing
                out = json.dumps(payload, indent=2)
                return out
        payload = {"status": "error", "description": "Unable to find specified job_title."}
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "missingLicenses",
                "description": "Finds any licenses a job's default licenses from the rbac_group_map database that are not assigned to an employee.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "employee_id": {
                            "type": "string",
                            "description": "The employee to verify licenses for.",
                        },
                        "job_title": {
                            "type": "string",
                            "description": "The job title to compare licenses against.",
                        },
                    },
                    "required": ["employee_id", "job_title"],
                },
            },
        }
