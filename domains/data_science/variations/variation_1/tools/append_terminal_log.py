from tau_bench.envs.tool import Tool
import json
from typing import Any

class AppendTerminalLog(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        command: str = None,
        exit_code: int = 0,
        printed_message: str = "",
        printed_ts: str = "1970-01-01T00:00:00Z",
        stderr: str = "",
        stdout: str = ""
    ) -> str:
        err = _require({"command": command}, ["command"])
        if err:
            return err
        tbl = data.setdefault("terminal_log", [])
        row = {
            "command": command,
            "exit_code": exit_code,
            "stdout": stdout,
            "stderr": stderr,
            "printed_message": printed_message,
            "printed_ts": printed_ts,
        }
        payload = _append(tbl, row)
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AppendTerminalLog",
                "description": "Appends a terminal log row (deterministic fields only).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "command": {"type": "string"},
                        "exit_code": {"type": "integer"},
                        "stdout": {"type": "string"},
                        "stderr": {"type": "string"},
                        "printed_message": {"type": "string"},
                        "printed_ts": {"type": "string"},
                    },
                    "required": ["command"],
                },
            },
        }
