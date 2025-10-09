from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class LicenseRequiresRenewal(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], num_days: int = None) -> str:
        if num_days is None:
            payload = {"status": "error", "reason": "The num_days field is required."}
            out = json.dumps(
                payload, indent=2,
            )
            return out

        inventory = data.get("license_inventory")
        licenses = []

        dt_now = datetime.fromisoformat(FIXED_NOW)

        for license in inventory:
            dt_audit = datetime.fromisoformat(license["last_audit_at"])
            if (dt_now - dt_audit).days > num_days:
                licenses.append(license["license_id"])
        payload = licenses
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "licenseRequiresRenewal",
                "description": "Returns the license_id of any license audited over num_days ago.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "num_days": {
                            "type": "string",
                            "description": "The number of days to filter by.",
                        },
                    },
                    "required": ["num_days"],
                },
            },
        }
