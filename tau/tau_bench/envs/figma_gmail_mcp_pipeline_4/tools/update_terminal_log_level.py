from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class UpdateTerminalLogLevel(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        message: str,
        log_level: str = "INFO",
        source_component: str = None,
        workflow_id: str = None,
        max_log_entries: int = 1000
    ) -> str:
        """
        Includes new terminal log entries and oversees log retention.
        """
        if not message:
            payload = {"error": "message is required."}
            out = json.dumps(payload)
            return out

        # Check the correctness of log level
        valid_levels = ["DEBUG", "INFO", "WARN", "ERROR", "CRITICAL"]
        if log_level not in valid_levels:
            payload = {
                "error": f"Invalid log_level. Must be one of: {', '.join(valid_levels)}"
            }
            out = json.dumps(payload)
            return out

        terminal_logs = data.get("terminal_logs", [])

        # Generate a new log entry
        new_log_entry = {
            "log_ts": datetime.now().isoformat(),
            "message": f"{log_level}: {message}",
            "level": log_level,
            "component": source_component,
            "workflow_id": workflow_id,
        }

        # Include entry in logs
        terminal_logs.append(new_log_entry)

        # Enforce log retention by retaining only the latest entries
        if len(terminal_logs) > max_log_entries:
            # Order by timestamp and retain the latest
            terminal_logs.sort(key=lambda x: x.get("log_ts", ""))
            # Eliminate the oldest entries
            excess_count = len(terminal_logs) - max_log_entries
            for _ in range(excess_count):
                terminal_logs.pop(0)
        payload = {
            "success": True,
            "log_entry": new_log_entry,
            "total_log_entries": len(terminal_logs),
            "logged_at": datetime.now().isoformat(),
        }
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "updateTerminalLogLevel",
                "description": "Adds new terminal log entries with specified log levels and manages log retention for workflow tracking and debugging.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "message": {
                            "type": "string",
                            "description": "The log message to add.",
                        },
                        "log_level": {
                            "type": "string",
                            "description": "The log level. Must be one of: DEBUG, INFO, WARN, ERROR, CRITICAL.",
                        },
                        "source_component": {
                            "type": "string",
                            "description": "Optional component or service generating the log entry.",
                        },
                        "workflow_id": {
                            "type": "string",
                            "description": "Optional workflow ID to associate with the log entry.",
                        },
                        "max_log_entries": {
                            "type": "integer",
                            "description": "Maximum number of log entries to retain (default: 1000).",
                        },
                    },
                    "required": ["message"],
                },
            },
        }
