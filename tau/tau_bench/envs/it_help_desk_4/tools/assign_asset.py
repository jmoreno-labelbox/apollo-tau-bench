# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class AssignAsset(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        asset_id = kwargs.get("asset_id")
        employee_id = kwargs.get("employee_id")
        assets = list(data.get("it_assets", {}).values())
        asset = next((a for a in assets if a.get("asset_id") == asset_id), None)
        if not asset:
            return json.dumps({"error": f"Asset {asset_id} not found."}, indent=2)
        asset["assigned_to"] = employee_id
        asset["status"] = "READY FOR PICKUP"
        asset["mdm_enrolled"] = True
        return json.dumps(asset, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "assign_asset", "description": "Assign an IT asset to an employee.", "parameters": {"type": "object", "properties": {"asset_id": {"type": "string"}, "employee_id": {"type": "string"}}, "required": ["asset_id", "employee_id"]}}}
