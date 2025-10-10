# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetUserAsset(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        employee_id = kwargs.get("employee_id")
        assets = list(data.get("it_assets", {}).values())
        asset = next((a for a in assets if a.get("assigned_to") == employee_id), None)
        if not asset:
            return json.dumps({"employee_id": employee_id, "asset": None}, indent=2)
        return json.dumps(asset, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "get_user_asset", "description": "Find an IT asset assigned to a specific employee.", "parameters": {"type": "object", "properties": {"employee_id": {"type": "string"}}, "required": ["employee_id"]}}}
