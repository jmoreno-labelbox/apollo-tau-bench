from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class AssignAsset(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], asset_id: str = None, employee_id: str = None, timestamp: str = None) -> str:
        assets = data.get("it_assets", [])
        asset = next((a for a in assets if a.get("asset_id") == asset_id), None)
        if not asset:
            payload = {"error": f"Asset {asset_id} not found."}
            out = json.dumps(payload, indent=2)
            return out
        asset["assigned_to"] = employee_id
        asset["status"] = "READY FOR PICKUP"
        asset["mdm_enrolled"] = True
        payload = asset
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AssignAsset",
                "description": "Assign an IT asset to an employee.",
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
