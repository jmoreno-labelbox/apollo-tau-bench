from tau_bench.envs.tool import Tool
import json
from typing import Any

class ScheduleDeviceMDMRemoval(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], asset_id: str = None, last_day: str = None) -> str:
        payload = {
            "asset_id": asset_id,
            "removal_scheduled_for": last_day,
            "status": "pending_removal",
        }
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "scheduleDeviceMdmRemoval",
                "description": "Schedules a device for removal from MDM on a specific date.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "asset_id": {"type": "string"},
                        "last_day": {"type": "string"},
                    },
                    "required": ["asset_id", "last_day"],
                },
            },
        }
