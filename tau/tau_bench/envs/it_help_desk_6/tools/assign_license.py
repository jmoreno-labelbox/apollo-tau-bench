# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class AssignLicense(Tool):
    @staticmethod
    def invoke(
        data: Dict[str, Any],
        assignment_id: str,
        account_id: str,
        employee_id: str,
        license_id: str,
        assigned_at: str,
    ) -> str:
        inv = _find_one(data["license_inventory"], license_id=license_id)
        if not inv:
            return json.dumps({"status": "error", "reason": "license_not_found"})
        if inv["used_seats"] + inv["reserved_seats"] + 1 > inv["total_seats"]:
            return json.dumps({"status": "error", "reason": "no_capacity"})

        # Directly modify the dictionary in the list
        for item in data["license_inventory"]:
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
        return json.dumps({"status": "ok", "assignment": row, "inventory": inv})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "assign_license",
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
                    "required": ["assignment_id", "account_id", "employee_id", "license_id", "assigned_at"],
                },
            },
        }
