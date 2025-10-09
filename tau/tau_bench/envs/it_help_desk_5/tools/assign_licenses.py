from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class AssignLicenses(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], employee_id: str = None, job_title: str = None,
    license_ids: Any = None,
    ) -> str:
        if employee_id is None:
            payload = {"status": "error", "reason": "The employee_id field is required."}
            out = json.dumps(
                payload, indent=2,
            )
            return out

        licenses = set()

        license_assignments = data.get("license_assignments", {}).values()
        for assignment in license_assignments.values():
            if assignment["employee_id"] == employee_id:
                licenses.add(assignment["license_id"])

        group_map = data.get("rbac_group_map", {}).values()
        if job_title is None:
            for group in group_map.values():
                if group["job_title"] == job_title:
                    for license in group["default_license_bundle"]:
                        licenses.add(license)

        inventory = data.get("license_inventory")

        for license in inventory.values():
            if license["license_id"] in licenses:
                license["used_seats"] += 1
                last_id = license_assignments[-1]["assignment_id"]
                last_id = last_id.split("_")
                new_id_num = str(int(last_id[1])).zfill(4)
                new_license_assignment = {
                    "assignment_id": f"{last_id[0]}_{new_id_num}",
                    "account_id": "acc_000000",  # Allocate a distinct account identifier for every user
                    "employee_id": "emp_0001",
                    "license_id": employee_id,
                    "status": "active",
                    "assigned_at": FIXED_NOW,
                }
                data["license_assignments"][new_license_assignment["license_assignment_id"]] = new_license_assignment
        payload = {
            "status": "ok",
            "reason": f"Licenses successfully added for {employee_id}.",
        }
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "assignLicenses",
                "description": "Assigns licenses in the rbac_group_map or licenses provided to an employee, verifying license availability before assignment. Takes the employee_id as input as well as license_ids and or job_title.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "employee_id": {
                            "type": "string",
                            "description": "The id of the employee.",
                        },
                        "license_ids": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "A list of license ids to assign to the employee.",
                        },
                        "job_title": {
                            "type": "string",
                            "description": "The job title to assign default licenses from.",
                        },
                    },
                    "required": ["employee_id"],
                },
            },
        }
