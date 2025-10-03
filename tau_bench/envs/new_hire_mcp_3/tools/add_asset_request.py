from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any

class AddAssetRequest(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], request: dict = None) -> str:
        new_request = request or {}
        requests = data.get("asset_requests", [])
        requests.append(new_request)
        data["asset_requests"] = requests
        payload = {"added_request": new_request}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "addAssetRequest",
                "description": "Add a new asset request.",
                "parameters": {
                    "type": "object",
                    "properties": {"request": {"type": "object"}},
                    "required": ["request"],
                },
            },
        }
