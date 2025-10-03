from tau_bench.envs.tool import Tool
import json
from typing import Any

class AppendTerminalLogEntry(Tool):
    """Adds a single entry to terminal_log arrays in the first record or initializes a new one."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        command: str,
        exit_code: int,
        stdout: str,
        stderr: str,
        printed_message: str,
        printed_ts: str,
    ) -> str:
        rows = data.setdefault("terminal_log", [])
        if not rows:
            rows.append(
                {
                    "commands": [],
                    "exit_codes": [],
                    "stdouts": [],
                    "stderrs": [],
                    "printed_messages": [],
                    "printed_ts": [],
                }
            )
        row = rows[0]
        row.setdefault("commands", []).append(command)
        row.setdefault("exit_codes", []).append(exit_code)
        row.setdefault("stdouts", []).append(stdout)
        row.setdefault("stderrs", []).append(stderr)
        row.setdefault("printed_messages", []).append(printed_message)
        row.setdefault("printed_ts", []).append(printed_ts)
        payload = {"status": "appended", "index": len(row["commands"]) - 1}
        out = json.dumps(payload)
        return out

    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AppendTerminalLogEntry",
                "description": "Appends a single entry to terminal_log arrays.",
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
                    "required": [
                        "command",
                        "exit_code",
                        "stdout",
                        "stderr",
                        "printed_message",
                        "printed_ts",
                    ],
                },
            },
        }
