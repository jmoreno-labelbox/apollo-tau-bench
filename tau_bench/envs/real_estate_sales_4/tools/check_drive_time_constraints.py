from tau_bench.envs.tool import Tool
import json
from typing import Any

class CheckDriveTimeConstraints(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], property_ids: list = None, max_minutes: int = 30) -> str:
        if not property_ids:
            payload = {"error": "property_ids is required"}
            out = json.dumps(payload, indent=2)
            return out

        feasible = len(property_ids) <= 4

        result = {
            "feasible": feasible,
            "property_count": len(property_ids),
            "max_minutes_per_hop": max_minutes,
            "estimated_total_time": len(property_ids) * 25,
            "properties_checked": property_ids,
        }
        payload = result
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "checkDriveTimeConstraints",
                "description": "Check if properties can be visited within time constraints",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "property_ids": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "List of property IDs to check",
                        },
                        "max_minutes": {
                            "type": "integer",
                            "description": "Maximum minutes allowed between stops",
                        },
                    },
                    "required": ["property_ids"],
                },
            },
        }
