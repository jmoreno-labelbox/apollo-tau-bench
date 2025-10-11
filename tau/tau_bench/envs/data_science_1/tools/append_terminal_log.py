# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _require


class AppendTerminalLog(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], command, exit_code = 0, printed_message = "", printed_ts = "1970-01-01T00:00:00Z", stderr = "", stdout = "") -> str:
        err = _require(kwargs, ["command"])
        if err: return err
        tbl = data.setdefault("terminal_log", [])
        row = {
            "command": command, "exit_code": exit_code,
            "stdout": stdout, "stderr": stderr,
            "printed_message": printed_message,
            "printed_ts": printed_ts
        }
        return json.dumps(_append(tbl, row), indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {
            "name": "append_terminal_log",
            "description": "Appends a terminal log row (deterministic fields only).",
            "parameters": {"type": "object", "properties": {
                "command": {"type": "string"}, "exit_code": {"type": "integer"},
                "stdout": {"type": "string"}, "stderr": {"type": "string"},
                "printed_message": {"type": "string"}, "printed_ts": {"type": "string"}},
                "required": ["command"]}}}
