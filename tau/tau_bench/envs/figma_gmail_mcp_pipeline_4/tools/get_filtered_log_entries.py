from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime
from typing import Any

class GetFilteredLogEntries(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        log_level: str = None,
        message_pattern: str = None,
        after_timestamp: str = None,
        before_timestamp: str = None,
        component: str = None
    ) -> str:
        """
        Obtains terminal logs with filtering and summarization features.
        """
        terminal_logs = data.get("terminal_logs", [])

        # Sort logs based on specified criteria
        results = []
        for log in terminal_logs:
            # Implement filter for log level
            if log_level:
                log_message = log.get("message", "")
                if not log_message.startswith(f"{log_level}:"):
                    continue

            # Implement filter for message pattern
            if message_pattern:
                if message_pattern.lower() not in log.get("message", "").lower():
                    continue

            # Implement filter for component
            if component:
                if log.get("component") != component:
                    continue

            # Enforce timestamp filters
            if after_timestamp:
                log_time = log.get("log_ts", "")
                if log_time < after_timestamp:
                    continue

            if before_timestamp:
                log_time = log.get("log_ts", "")
                if log_time > before_timestamp:
                    continue

            results.append(log)

        # Generate a summary categorized by log level
        level_counts = {}
        for log in results:
            message = log.get("message", "")
            level = message.split(":")[0] if ":" in message else "UNKNOWN"
            level_counts[level] = level_counts.get(level, 0) + 1

        summary = {
            "total_logs": len(results),
            "level_breakdown": level_counts,
            "logs": results,
        }
        payload = summary
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetFilteredLogEntries",
                "description": "Retrieves terminal logs with filtering and summary capabilities including log level breakdown.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "log_level": {
                            "type": "string",
                            "description": "Filter logs by level (DEBUG, INFO, WARNING, ERROR, CRITICAL).",
                        },
                        "message_pattern": {
                            "type": "string",
                            "description": "Filter logs containing this message pattern.",
                        },
                        "after_timestamp": {
                            "type": "string",
                            "description": "Filter logs after this ISO timestamp.",
                        },
                        "before_timestamp": {
                            "type": "string",
                            "description": "Filter logs before this ISO timestamp.",
                        },
                        "component": {
                            "type": "string",
                            "description": "Filter logs by component name.",
                        },
                    },
                },
            },
        }
