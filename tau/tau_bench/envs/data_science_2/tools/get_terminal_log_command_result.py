# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetTerminalLogCommandResult(Tool):
    """
    Retrieves a terminal_log entry by exact command string.
    """
    @staticmethod
    def invoke(data: Dict[str, Any], command: str) -> str:
        rows = list(data.get("terminal_log", {}).values())
        for row in rows:
            cmds = row.get("commands", [])
            if command in cmds:
                i = cmds.index(command)
                out = {
                    "command": command,
                    "exit_code": row.get("exit_codes", [None]*len(cmds))[i] if i < len(row.get("exit_codes", [])) else None,
                    "stdout": row.get("stdouts", [None]*len(cmds))[i] if i < len(row.get("stdouts", [])) else None,
                    "stderr": row.get("stderrs", [None]*len(cmds))[i] if i < len(row.get("stderrs", [])) else None,
                    "printed_message": row.get("printed_messages", [None]*len(cmds))[i] if i < len(row.get("printed_messages", [])) else None,
                    "printed_ts": row.get("printed_ts", [None]*len(cmds))[i] if i < len(row.get("printed_ts", [])) else None
                }
                return json.dumps(out)
        return json.dumps({"error": "command not found", "command": command})

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_terminal_log_command_result",
                "description": "Retrieves a terminal_log entry by exact command.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "command": {"type": "string", "description": "Exact command string to look up."}
                    },
                    "required": ["command"]
                }
            }
        }
