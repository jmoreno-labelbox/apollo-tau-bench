# Copyright owned by Sierra.

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateCarrierStatus(Tool):
    """Updates the status of a carrier."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        carrier_name, status = map(kwargs.get, ["carrier_name", "status"])
        if not all([carrier_name, status]):
            return json.dumps({"error": "carrier_name and status are required."}, indent=2)
        carrier_to_update = next((c for c in data.get('carriers', []) if c.get('carrier_name') == carrier_name), None)
        if not carrier_to_update:
            return json.dumps({"error": f"Carrier '{carrier_name}' not found."}, indent=2)
        carrier_to_update['active_status'] = status
        return json.dumps({"carrier_id": carrier_to_update.get('carrier_id'), "carrier_name": carrier_name, "new_status": status}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "update_carrier_status", "description": "Updates the operational status of a carrier (e.g., True, False, 'Under Review').", "parameters": {"type": "object", "properties": {"carrier_name": {"type": "string"}, "status": {"type": "string", "description": "The new status to set for the carrier."}}, "required": ["carrier_name", "status"]}}}
