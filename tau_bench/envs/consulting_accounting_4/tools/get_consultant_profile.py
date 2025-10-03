from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any

class GetConsultantProfile(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], consultant_id: str = None) -> str:
        row = next(
            (c for c in data.get("consultants", []) if c.get("consultant_id") == consultant_id),
            None,
        )
        if not row:
            payload = {"error": f"Consultant '{consultant_id}' not found"}
            out = json.dumps(payload, indent=2)
            return out
        payload = row
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetConsultantProfile",
                "description": "Fetch the consultant profile row.",
                "parameters": {
                    "type": "object",
                    "properties": {"consultant_id": {"type": "string"}},
                    "required": ["consultant_id"],
                },
            },
        }
