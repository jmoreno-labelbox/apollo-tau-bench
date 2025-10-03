from tau_bench.envs.tool import Tool
import json
import re
from datetime import datetime, timezone
from typing import Any

class ReadAssetRequest(Tool):
    @staticmethod
    def invoke(data, request_id: str) -> str:
        row = next(
            (r for r in data.get("asset_requests", []) if r.get("request_id") == request_id),
            None,
        )
        payload = {"asset_request": row} if row else {"error": f"request_id {request_id} not found"}
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "ReadAssetRequest",
                "parameters": {
                    "type": "object",
                    "properties": {"request_id": {"type": "string"}},
                    "required": ["request_id"],
                },
            },
        }
