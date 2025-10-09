from tau_bench.envs.tool import Tool
import json
from collections import Counter, defaultdict
from typing import Any

class AppendTerminal(Tool):
    @staticmethod
    def invoke(data: dict[str, Any], message: str = None) -> str:
        if not message:
            payload = {"error": "message is required."}
            out = json.dumps(payload, indent=2)
            return out
        entry = {"printed_ts": get_current_timestamp(), "message": str(message)}
        _terminal(data).append(entry)
        payload = entry
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info():
        pass
        return {
            "type": "function",
            "function": {
                "name": "AppendTerminal",
                "description": "Appends a message to terminal log with timestamp.",
                "parameters": {
                    "type": "object",
                    "properties": {"message": {"type": "string"}},
                    "required": ["message"],
                },
            },
        }
