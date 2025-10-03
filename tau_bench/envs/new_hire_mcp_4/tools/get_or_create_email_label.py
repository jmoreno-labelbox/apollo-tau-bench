from tau_bench.envs.tool import Tool
import json
import re
from datetime import datetime, timezone
from typing import Any

class GetOrCreateEmailLabel(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], name: str) -> str:
        label_id = _get_or_create_label_id(data, name)
        payload = {"label_id": label_id, "name": name}
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetOrCreateEmailLabel",
                "description": "Get or create label by name.",
                "parameters": {
                    "type": "object",
                    "properties": {"name": {"type": "string"}},
                    "required": ["name"],
                },
            },
        }
