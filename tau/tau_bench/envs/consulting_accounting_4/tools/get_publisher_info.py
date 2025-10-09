from tau_bench.envs.tool import Tool
import json
from datetime import datetime
from typing import Any

class GetPublisherInfo(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], publisher_id: str = None) -> str:
        pid = publisher_id
        row = next(
            (p for p in data.get("publishers", []) if p.get("publisher_id") == pid),
            None,
        )
        if not row:
            payload = {"error": f"Publisher '{pid}' not found"}
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
                "name": "GetPublisherInfo",
                "description": "Fetch a publisher record.",
                "parameters": {
                    "type": "object",
                    "properties": {"publisher_id": {"type": "string"}},
                    "required": ["publisher_id"],
                },
            },
        }
