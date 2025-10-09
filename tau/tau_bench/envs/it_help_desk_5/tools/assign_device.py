from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class AssignDevice(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], employee_id: str = None, asset_type: str = None) -> str:
        if employee_id is None or asset_type is None:
            payload = {
                    "status": "error",
                    "reason": "The employee_id and asset_type fields are required.",
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        assets = data.get("it_assets")

        for asset in assets:
            if asset["asset_type"] == asset_type and asset["status"] == "in_stock":
                asset["status"] = "assigned"
                asset["assigned_to"] = employee_id
                payload = {"status": "ok", "device": asset}
                out = json.dumps(payload, indent=2)
                return out
        payload = {"status": "error", "description": "Unable to find available asset."}
        out = json.dumps(
            payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "assignDevice",
                "description": "Assigns an employee a device of a specified type.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "employee_id": {
                            "type": "string",
                            "description": "The id of the employee.",
                        },
                        "asset_type": {
                            "type": "string",
                            "description": "The type of asset to assign to an employee.",
                        },
                    },
                    "required": ["employee_id", "asset_type"],
                },
            },
        }
