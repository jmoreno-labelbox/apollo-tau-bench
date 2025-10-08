from tau_bench.envs.tool import Tool
import json
from typing import Any

class UpdateLicenseInventory(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], license_id: str = None, operation: str = None) -> str:
        inventory = data.get("license_inventory", [])
        license_info = next(
            (lic for lic in inventory if lic.get("license_id") == license_id), None
        )
        if not license_info:
            payload = {"error": f"License ID {license_id} not found in inventory."}
            out = json.dumps(payload, indent=2)
            return out
        if operation == "increment":
            license_info["used_seats"] += 1
        elif operation == "decrement":
            license_info["used_seats"] = max(0, license_info.get("used_seats", 0) - 1)
        else:
            payload = {"error": "Operation must be 'increment' or 'decrement'."}
            out = json.dumps(payload, indent=2)
            return out
        payload = {
            "license_id": license_id,
            "new_used_seats": license_info["used_seats"],
            "operation": operation,
        }
        out = json.dumps(payload, indent=2)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "UpdateLicenseInventory",
                "description": "Atomically increment or decrement the used_seats count for a license in inventory.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "license_id": {"type": "string"},
                        "operation": {"type": "string"},
                    },
                    "required": ["license_id", "operation"],
                },
            },
        }
