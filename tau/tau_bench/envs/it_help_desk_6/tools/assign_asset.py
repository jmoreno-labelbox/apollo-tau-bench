from tau_bench.envs.tool import Tool
import json
from typing import Any

class AssignAsset(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], asset_id: str, employee_id: str) -> str:
        pass
        asset = _find_one(data["it_assets"], asset_id=asset_id)
        if not asset:
            payload = {"status": "error", "reason": "asset_not_found"}
            out = json.dumps(payload)
            return out
        asset["assigned_to"] = employee_id
        asset["status"] = "assigned"
        payload = {"status": "ok", "asset": asset}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AssignAsset",
                "description": "Assign an asset to an employee and set status to 'assigned'.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "asset_id": {"type": "string"},
                        "employee_id": {"type": "string"},
                    },
                    "required": ["asset_id", "employee_id"],
                },
            },
        }
