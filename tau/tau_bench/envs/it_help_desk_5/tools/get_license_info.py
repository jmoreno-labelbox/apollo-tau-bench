from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetLicenseInfo(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], license_name: str = None) -> str:
        if license_name is None:
            payload = {"status": "error", "reason": "The license_name field is required."}
            out = json.dumps(
                payload, indent=2,
            )
            return out

        inventory = data.get("license_inventory")
        assignments = data.get("license_assignments")

        for license in inventory:
            if license["name"] == license_name:
                assigned_licenses = []
                for assignment in assignments:
                    if assignment["license_id"] == license["license_id"]:
                        assigned_licenses.append(assignment)
                license_overview = {"info": license, "assignments": assigned_licenses}
                payload = license_overview
                out = json.dumps(payload, indent=2)
                return out
        payload = {"status": "error", "reason": "Could not find specified license."}
        out = json.dumps(
            payload, indent=2
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "getLicenseInfo",
                "description": "Gets all info associated with a specific license.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "license_name": {
                            "type": "string",
                            "description": "The name of the license.",
                        },
                    },
                    "required": ["license_name"],
                },
            },
        }
