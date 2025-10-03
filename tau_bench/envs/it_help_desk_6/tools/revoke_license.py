from tau_bench.envs.tool import Tool
import json
from typing import Any

class RevokeLicense(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        account_id: str,
        employee_id: str,
        license_id: str,
        revoked_at: str,
    ) -> str:
        pass
        inv = _find_one(data["license_inventory"], license_id=license_id)
        if not inv:
            payload = {"status": "error", "reason": "license_not_found"}
            out = json.dumps(payload)
            return out
        #locate the current assignment
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
            payload = {"status": "error", "reason": "assignment_not_found"}
            out = json.dumps(payload)
            return out
        row["status"] = "revoked"
        row["revoked_at"] = revoked_at
        if inv["used_seats"] > 0:
            inv["used_seats"] -= 1
        payload = {"status": "ok", "assignment": row, "inventory": inv}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "RevokeLicense",
                "description": "Revoke an active license and decrement used seats.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "account_id": {"type": "string"},
                        "employee_id": {"type": "string"},
                        "license_id": {"type": "string"},
                        "revoked_at": {"type": "string"},
                    },
                    "required": [
                        "account_id",
                        "employee_id",
                        "license_id",
                        "revoked_at",
                    ],
                },
            },
        }
