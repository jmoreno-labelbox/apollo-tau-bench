# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool




def _find_one(collection: List[Dict[str, Any]], ) -> Optional[Dict[str, Any]]:
    for row in collection:
        if all(row.get(k) == v for k, v in filters.items()):
            return row
    return None

class AssignAsset(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], asset_id: str, employee_id: str) -> str:
        asset = _find_one(data["it_assets"], asset_id=asset_id)
        if not asset:
            return json.dumps({"status": "error", "reason": "asset_not_found"})
        asset["assigned_to"] = employee_id
        asset["status"] = "assigned"
        return json.dumps({"status": "ok", "asset": asset})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "assign_asset",
                "description": "Assign an asset to an employee and set status to 'assigned'.",
                "parameters": {
                    "type": "object",
                    "properties": {"asset_id": {"type": "string"}, "employee_id": {"type": "string"}},
                    "required": ["asset_id", "employee_id"],
                },
            },
        }