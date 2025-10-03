from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime
from typing import Any

class AddTerminalLogEntry(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        component: str = None,
        log_level: str = "INFO",
        log_message: str = None,
        user_email: str = None
    ) -> str:
        """
        Includes new terminal log entries and oversees log level filtering.
        """
        if not log_message:
            payload = {"error": "log_message is required."}
            out = json.dumps(payload)
            return out

        # Check the correctness of log level
        valid_levels = ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]
        if log_level not in valid_levels:
            payload = {
                "error": f"Invalid log level. Must be one of: {', '.join(valid_levels)}"
            }
            out = json.dumps(payload)
            return out

        terminal_logs = data.get("terminal_logs", [])

        # Generate a new log entry
        new_log = {
            "log_ts": datetime.now().isoformat(),
            "message": f"{log_level}: {log_message}",
        }

        # Include optional metadata
        if component:
            new_log["component"] = component
        if user_email:
            new_log["user_email"] = user_email

        # Include in logs
        terminal_logs.append(new_log)
        payload = {"success": True, "log_entry": new_log, "total_logs": len(terminal_logs)}
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AddTerminalLogEntry",
                "description": "Adds new terminal log entries and manages log level filtering with optional metadata.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "log_message": {
                            "type": "string",
                            "description": "The log message content to add.",
                        },
                        "log_level": {
                            "type": "string",
                            "description": "The log level (DEBUG, INFO, WARNING, ERROR, CRITICAL). Default: INFO.",
                        },
                        "component": {
                            "type": "string",
                            "description": "Optional component name for the log entry.",
                        },
                        "user_email": {
                            "type": "string",
                            "description": "Optional user email associated with the log entry.",
                        },
                    },
                    "required": ["log_message"],
                },
            },
        }
