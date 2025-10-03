from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any

class GetStatusForAdSet(Tool):
    """Fetches the current status of a specific ad set."""

    @staticmethod
    def invoke(data: dict[str, Any], adset_id: str = None) -> str:
        adsets = data.get("adsets", [])

        for adset in adsets:
            if adset.get("adset_id") == adset_id:
                payload = {"status": adset.get("status")}
                out = json.dumps(payload)
                return out
        payload = {"error": f"Ad set with ID '{adset_id}' not found."}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetStatusForAdset",
                "description": "Retrieves the status for a specific ad set.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "adset_id": {
                            "type": "string",
                            "description": "The unique ID of the ad set.",
                        }
                    },
                    "required": ["adset_id"],
                },
            },
        }
