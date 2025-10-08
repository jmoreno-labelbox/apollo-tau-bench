from tau_bench.envs.tool import Tool
import json
from typing import Any

class CheckDriveTimeConstraints(Tool):
    """Verify if properties are accessible within the time limits."""

    @staticmethod
    def invoke(data: dict[str, Any], property_ids: list = None, max_minutes: int = 30) -> str:
        if not property_ids:
            payload = {"error": "property_ids is required"}
            out = json.dumps(payload, indent=2)
            return out

        # Emulate checking drive times
        feasible = (
            len(property_ids) <= 4
        )  # Basic rule: a maximum of 4 properties within the time constraint

        result = {
            "feasible": feasible,
            "property_count": len(property_ids),
            "max_minutes_per_hop": max_minutes,
            "estimated_total_time": len(property_ids)
            * 25,  # Average of 25 minutes per property
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
