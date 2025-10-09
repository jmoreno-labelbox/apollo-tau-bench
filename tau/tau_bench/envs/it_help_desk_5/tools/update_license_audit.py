from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any

class UpdateLicenseAudit(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], license_id: str = None) -> str:
        if license_id is None:
            payload = {"status": "error", "description": "The license_id field is required."}
            out = json.dumps(
                payload, indent=2,
            )
            return out

        inventory = data.get("license_inventory")

        for license in inventory:
            if license["license_id"] == license_id:
                license["last_audit_at"] = FIXED_NOW
                payload = {
                        "status": "ok",
                        "description": f"Successfully updated {license_id}.",
                    }
                out = json.dumps(
                    payload, indent=2,
                )
                return out
        payload = {"status": "error", "description": f"Unable to find {license_id}."}
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "updateLicenseAudit",
                "description": "Updates a liscense's audit date",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "license_id": {
                            "type": "string",
                            "description": "The license to update.",
                        },
                    },
                    "required": ["license_id"],
                },
            },
        }
