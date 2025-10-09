from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any

class DeviceAssignment(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], employee_id: str = None, unassign: bool = False) -> str:
        if employee_id is None:
            payload = {"status": "error", "reason": "The employee_id field is required."}
            out = json.dumps(
                payload, indent=2,
            )
            return out

        assets = data.get("it_assets")
        assigned_assets = []

        for asset in assets:
            if asset["assigned_to"] == employee_id:
                if unassign:
                    asset["status"] = "in_stock"
                    asset["assigned_to"] = None
                assigned_assets.append(asset)

        if unassign:
            payload = {
                    "status": "ok",
                    "reason": f"Successfully unassigned all devices from {employee_id}.",
                }
            out = json.dumps(
                payload, indent=2,
            )
            return out
        else:
            payload = assigned_assets
            out = json.dumps(payload, indent=2)
            return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "deviceAssignment",
                "description": "Updates or returns a list of devices assigned to an employee",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "employee_id": {
                            "type": "string",
                            "description": "The id of the employee.",
                        },
                        "unassign": {
                            "type": "boolean",
                            "description": "Whether to unassign devices.",
                        },
                    },
                    "required": ["employee_id"],
                },
            },
        }
