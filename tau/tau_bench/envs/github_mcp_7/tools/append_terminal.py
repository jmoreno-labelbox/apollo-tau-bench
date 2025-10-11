# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool




def _terminal(data: Dict[str, Any]) -> List[Dict[str, Any]]:
    return data.setdefault("terminal", [])

class AppendTerminal(Tool):
    """Append a line to the in-memory terminal log."""
    @staticmethod
    def invoke(data: Dict[str, Any], line) -> str:
        cmd = line or ""
        _terminal(data).append({"line": cmd, "when": get_current_timestamp()})
        return json.dumps({"ok": True})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "append_terminal",
                "description": "Append a line to an in-memory terminal log.",
                "parameters": {"type": "object", "properties": {"line": {"type": "string"}}, "required": ["line"]}
            },
        }