# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class RevokeLicense(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], account_id: str, employee_id: str, license_id: str, revoked_at: str) -> str:
        inv = _find_one(data["license_inventory"], license_id=license_id)
        if not inv:
            return json.dumps({"status": "error", "reason": "license_not_found"})
        # retrieve current assignment
        row = None
        for a in data["license_assignments"]:
            if (
                a["account_id"] == account_id
                and a["employee_id"] == employee_id
                and a["license_id"] == license_id
                and a["status"] == "active"
            ):
                row = a
                break
        if not row:
            return json.dumps({"status": "error", "reason": "assignment_not_found"})
        row["status"] = "revoked"
        row["revoked_at"] = revoked_at
        if inv["used_seats"] > 0:
            inv["used_seats"] -= 1
        return json.dumps({"status": "ok", "assignment": row, "inventory": inv})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "revoke_license",
                "description": "Revoke an active license and decrement used seats.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "account_id": {"type": "string"},
                        "employee_id": {"type": "string"},
                        "license_id": {"type": "string"},
                        "revoked_at": {"type": "string"},
                    },
                    "required": ["account_id", "employee_id", "license_id", "revoked_at"],
                },
            },
        }
