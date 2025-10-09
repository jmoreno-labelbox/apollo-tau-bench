from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db)
    return db

class UnassignLicenses(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], employee_id: str = None, license_ids: list = None) -> str:
        if employee_id is None:
            payload = {"status": "error", "reason": "The employee_id field is required."}
            out = json.dumps(
                payload, indent=2,
            )
            return out

        if license_ids is None:
            license_ids = []

        assignments = data.get("license_assignments")
        inventory = data.get("license_inventory")

        for assignment in assignments.values():
            if assignment["employee_id"] == employee_id and (
                len(license_ids) == 0 or assignment["license_id"] in license_ids
            ):
                assignment["status"] = "inactive"
                license_ids.append(assignment["license_id"])

        license_ids = set(license_ids)

        for license in inventory.values():
            if license["license_id"] in license_ids:
                license["used_seats"] -= 1
        payload = {
                "status": "ok",
                "reason": f"Licenses successfully removed for {employee_id}",
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
                "name": "unassignLicenses",
                "description": "Unssigns licenses from an employee and updates license_inventory. Takes the employee_id and license_ids as input. If no license_ids are supplied, removes all licenses from the employee.",
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
                            "description": "A list of license ids to unassign from the employee.",
                        },
                    },
                    "required": ["employee_id"],
                },
            },
        }
