# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool
from . import _require


class AppendTerminalLog(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        err = _require(kwargs, ["command"])
        if err: return err
        tbl = data.setdefault("terminal_log", [])
        row = {
            "command": kwargs["command"], "exit_code": kwargs.get("exit_code", 0),
            "stdout": kwargs.get("stdout", ""), "stderr": kwargs.get("stderr", ""),
            "printed_message": kwargs.get("printed_message", ""),
            "printed_ts": kwargs.get("printed_ts", "1970-01-01T00:00:00Z")
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
