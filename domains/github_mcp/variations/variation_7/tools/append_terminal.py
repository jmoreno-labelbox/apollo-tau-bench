from tau_bench.envs.tool import Tool
import json
from typing import Any

class AppendTerminal(Tool):
    """Add a line to the terminal log stored in memory."""

    @staticmethod
    def invoke(data: dict[str, Any], line: str = "") -> str:
        cmd = line or ""
        _terminal(data).append({"line": cmd, "when": get_current_timestamp()})
        payload = {"ok": True}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "appendTerminal",
                "description": "Append a line to an in-memory terminal log.",
                "parameters": {
                    "type": "object",
                    "properties": {"line": {"type": "string"}},
                    "required": ["line"],
                },
            },
        }
