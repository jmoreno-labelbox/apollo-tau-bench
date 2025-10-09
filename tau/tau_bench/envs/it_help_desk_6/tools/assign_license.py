from tau_bench.envs.tool import Tool
import json
from typing import Any

class AssignLicense(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        assignment_id: str,
        account_id: str,
        employee_id: str,
        license_id: str,
        assigned_at: str,
    ) -> str:
        pass
        inv = _find_one(data["license_inventory"], license_id=license_id)
        if not inv:
            payload = {"status": "error", "reason": "license_not_found"}
            out = json.dumps(payload)
            return out
        if inv["used_seats"] + inv["reserved_seats"] + 1 > inv["total_seats"]:
            payload = {"status": "error", "reason": "no_capacity"}
            out = json.dumps(payload)
            return out

        #Alter the dictionary within the list directly
        for item in data["license_inventory"].values():
            if item["license_id"] == license_id:
                item["used_seats"] += 1
                break

        row = {
            "assignment_id": assignment_id,
            "account_id": account_id,
            "employee_id": employee_id,
            "license_id": license_id,
            "status": "active",
            "assigned_at": assigned_at,
        }
        _append_row(data["license_assignments"], row)
        payload = {"status": "ok", "assignment": row, "inventory": inv}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AssignLicense",
                "description": "Assign a license and increment used seats deterministically.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "assignment_id": {"type": "string"},
                        "account_id": {"type": "string"},
                        "employee_id": {"type": "string"},
                        "license_id": {"type": "string"},
                        "assigned_at": {"type": "string"},
                    },
                    "required": [
                        "assignment_id",
                        "account_id",
                        "employee_id",
                        "license_id",
                        "assigned_at",
                    ],
                },
            },
        }
