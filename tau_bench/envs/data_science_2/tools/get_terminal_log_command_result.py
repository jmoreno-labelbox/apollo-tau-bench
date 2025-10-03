from tau_bench.envs.tool import Tool
import json
from typing import Any

class GetTerminalLogCommandResult(Tool):
    """Fetches a terminal_log entry using the precise command string."""

    @staticmethod
    def invoke(data: dict[str, Any], command: str, terminal_log: list[dict[str, Any]] = None) -> str:
        rows = terminal_log or []
        for row in rows:
            cmds = row.get("commands", [])
            if command in cmds:
                i = cmds.index(command)
                out = {
                    "command": command,
                    "exit_code": (
                        row.get("exit_codes", [None] * len(cmds))[i]
                        if i < len(row.get("exit_codes", []))
                        else None
                    ),
                    "stdout": (
                        row.get("stdouts", [None] * len(cmds))[i]
                        if i < len(row.get("stdouts", []))
                        else None
                    ),
                    "stderr": (
                        row.get("stderrs", [None] * len(cmds))[i]
                        if i < len(row.get("stderrs", []))
                        else None
                    ),
                    "printed_message": (
                        row.get("printed_messages", [None] * len(cmds))[i]
                        if i < len(row.get("printed_messages", []))
                        else None
                    ),
                    "printed_ts": (
                        row.get("printed_ts", [None] * len(cmds))[i]
                        if i < len(row.get("printed_ts", []))
                        else None
                    ),
                }
                payload = out
                out = json.dumps(payload)
                return out
        payload = {"error": "command not found", "command": command}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetTerminalLogCommandResult",
                "description": "Retrieves a terminal_log entry by exact command.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "command": {
                            "type": "string",
                            "description": "Exact command string to look up.",
                        }
                    },
                    "required": ["command"],
                },
            },
        }
