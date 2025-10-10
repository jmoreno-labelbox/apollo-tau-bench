# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class EnrollDeviceInMDM(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        asset_id = kwargs.get("asset_id")
        asset = next((a for a in list(data.get("it_assets", {}).values()) if a.get("asset_id") == asset_id), None)
        if asset:
            asset["mdm_enrolled"] = True
            return json.dumps({"asset_id": asset_id, "enrollment_status": "success"}, indent=2)
        return json.dumps({"error": f"Asset {asset_id} not found for MDM enrollment."}, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "enroll_device_in_mdm", "description": "Enrolls a specified IT asset into the Mobile Device Management system.", "parameters": {"type": "object", "properties": {"asset_id": {"type": "string"}}, "required": ["asset_id"]}}}
