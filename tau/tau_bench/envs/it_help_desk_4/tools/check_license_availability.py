# Copyright © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CheckLicenseAvailability(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        license_id = kwargs.get("license_id")
        inventory = list(data.get("license_inventory", {}).values())
        license_info = next((lic for lic in inventory if lic.get("license_id") == license_id), None)
        if not license_info:
            return json.dumps({"error": f"License ID {license_id} not found in inventory."}, indent=2)
        available = license_info.get("total_seats", 0) - license_info.get("used_seats", 0)
        return json.dumps({"license_id": license_id, "seats_available": available > 0, "available_count": available}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "check_license_availability", "description": "Check if there are available seats for a given license SKU.", "parameters": {"type": "object", "properties": {"license_id": {"type": "string"}}, "required": ["license_id"]}}}
