# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class UpdateTerminalLogLevel(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], message, source_component, workflow_id, log_level = 'INFO', max_log_entries = 1000) -> str:
        """
        Adds new terminal log entries and manages log retention.
        """

        if not message:
            return json.dumps({"error": "message is required."})

        # Check the validity of the log level.
        valid_levels = ['DEBUG', 'INFO', 'WARN', 'ERROR', 'CRITICAL']
        if log_level not in valid_levels:
            return json.dumps({"error": f"Invalid log_level. Must be one of: {', '.join(valid_levels)}"})

        terminal_logs = data.get('terminal_logs', [])

        # Generate a new log entry.
        new_log_entry = {
            "log_ts": datetime.now().isoformat(),
            "message": f"{log_level}: {message}",
            "level": log_level,
            "component": source_component,
            "workflow_id": workflow_id
        }

        # Insert log entry
        terminal_logs.append(new_log_entry)

        # Establish log retention by retaining only the latest entries.
        if len(terminal_logs) > max_log_entries:
            # Order by timestamp and retain the latest entry.
            terminal_logs.sort(key=lambda x: x.get('log_ts', ''))
            # Eliminate the earliest records.
            excess_count = len(terminal_logs) - max_log_entries
            for _ in range(excess_count):
                terminal_logs.pop(0)

        return json.dumps({
            "success": True,
            "log_entry": new_log_entry,
            "total_log_entries": len(terminal_logs),
            "logged_at": datetime.now().isoformat()
        })

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "update_terminal_log_level",
                "description": "Adds new terminal log entries with specified log levels and manages log retention for workflow tracking and debugging.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "message": {"type": "string", "description": "The log message to add."},
                        "log_level": {"type": "string", "description": "The log level. Must be one of: DEBUG, INFO, WARN, ERROR, CRITICAL."},
                        "source_component": {"type": "string", "description": "Optional component or service generating the log entry."},
                        "workflow_id": {"type": "string", "description": "Optional workflow ID to associate with the log entry."},
                        "max_log_entries": {"type": "integer", "description": "Maximum number of log entries to retain (default: 1000)."}
                    },
                    "required": ["message"]
                }
            }
        }
