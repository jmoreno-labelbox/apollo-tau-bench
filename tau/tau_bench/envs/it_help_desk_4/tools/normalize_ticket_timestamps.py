from tau_bench.envs.tool import Tool
import json
from typing import Any

class NormalizeTicketTimestamps(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], input_path: str = None, output_path: str = None, timezone: str = "UTC") -> str:
        payload = {
            "status": "normalized",
            "input_path": input_path,
            "output_path": output_path,
            "timezone": timezone,
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
                "name": "normalizeTicketTimestamps",
                "description": "Normalize ticket timestamps to specified timezone.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "input_path": {"type": "string"},
                        "output_path": {"type": "string"},
                        "timezone": {"type": "string"},
                    },
                    "required": ["input_path", "output_path"],
                },
            },
        }
