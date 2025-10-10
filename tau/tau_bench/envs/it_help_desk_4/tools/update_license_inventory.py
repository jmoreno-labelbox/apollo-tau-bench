# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateLicenseInventory(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        license_id = kwargs.get("license_id")
        operation = kwargs.get("operation")
        inventory = list(data.get("license_inventory", {}).values())
        license_info = next((lic for lic in inventory if lic.get("license_id") == license_id), None)
        if not license_info:
            return json.dumps({"error": f"License ID {license_id} not found in inventory."}, indent=2)
        if operation == "increment":
            license_info["used_seats"] += 1
        elif operation == "decrement":
            license_info["used_seats"] = max(0, license_info.get("used_seats", 0) - 1)
        else:
            return json.dumps({"error": "Operation must be 'increment' or 'decrement'."}, indent=2)
        return json.dumps({"license_id": license_id, "new_used_seats": license_info["used_seats"], "operation": operation}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "update_license_inventory", "description": "Atomically increment or decrement the used_seats count for a license in inventory.", "parameters": {"type": "object", "properties": {"license_id": {"type": "string"}, "operation": {"type": "string"}}, "required": ["license_id", "operation"]}}}
