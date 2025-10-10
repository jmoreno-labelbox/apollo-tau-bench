# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class AddTerminalLogEntry(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        """
        Adds new terminal log entries and manages log level filtering.
        """
        log_message = kwargs.get('log_message')
        log_level = kwargs.get('log_level', 'INFO')
        component = kwargs.get('component')
        user_email = kwargs.get('user_email')

        if not log_message:
            return json.dumps({"error": "log_message is required."})

        # Validate log level
        valid_levels = ['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']
        if log_level not in valid_levels:
            return json.dumps({"error": f"Invalid log level. Must be one of: {', '.join(valid_levels)}"})

        terminal_logs = data.get('terminal_logs', [])

        # Create new log entry
        new_log = {
            "log_ts": datetime.now().isoformat(),
            "message": f"{log_level}: {log_message}"
        }

        # Add optional metadata
        if component:
            new_log["component"] = component
        if user_email:
            new_log["user_email"] = user_email

        # Add to logs
        terminal_logs.append(new_log)

        return json.dumps({
            "success": True,
            "log_entry": new_log,
            "total_logs": len(terminal_logs)
        })

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "add_terminal_log_entry",
                "description": "Adds new terminal log entries and manages log level filtering with optional metadata.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "log_message": {"type": "string", "description": "The log message content to add."},
                        "log_level": {"type": "string", "description": "The log level (DEBUG, INFO, WARNING, ERROR, CRITICAL). Default: INFO."},
                        "component": {"type": "string", "description": "Optional component name for the log entry."},
                        "user_email": {"type": "string", "description": "Optional user email associated with the log entry."}
                    },
                    "required": ["log_message"]
                }
            }
        }
