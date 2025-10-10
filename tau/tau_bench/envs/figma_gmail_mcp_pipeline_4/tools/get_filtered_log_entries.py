# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetFilteredLogEntries(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        """
        Retrieves terminal logs with filtering and summary capabilities.
        """
        log_level = kwargs.get('log_level')
        message_pattern = kwargs.get('message_pattern')
        after_timestamp = kwargs.get('after_timestamp')
        before_timestamp = kwargs.get('before_timestamp')
        component = kwargs.get('component')

        terminal_logs = data.get('terminal_logs', [])

        # Filter logs by criteria
        results = []
        for log in terminal_logs:
            # Apply log level filter
            if log_level:
                log_message = log.get('message', '')
                if not log_message.startswith(f"{log_level}:"):
                    continue

            # Apply message pattern filter
            if message_pattern:
                if message_pattern.lower() not in log.get('message', '').lower():
                    continue

            # Apply component filter
            if component:
                if log.get('component') != component:
                    continue

            # Apply timestamp filters
            if after_timestamp:
                log_time = log.get('log_ts', '')
                if log_time < after_timestamp:
                    continue

            if before_timestamp:
                log_time = log.get('log_ts', '')
                if log_time > before_timestamp:
                    continue

            results.append(log)

        # Create summary by log level
        level_counts = {}
        for log in results:
            message = log.get('message', '')
            level = message.split(':')[0] if ':' in message else 'UNKNOWN'
            level_counts[level] = level_counts.get(level, 0) + 1

        summary = {
            "total_logs": len(results),
            "level_breakdown": level_counts,
            "logs": results
        }

        return json.dumps(summary, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_filtered_log_entries",
                "description": "Retrieves terminal logs with filtering and summary capabilities including log level breakdown.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "log_level": {"type": "string", "description": "Filter logs by level (DEBUG, INFO, WARNING, ERROR, CRITICAL)."},
                        "message_pattern": {"type": "string", "description": "Filter logs containing this message pattern."},
                        "after_timestamp": {"type": "string", "description": "Filter logs after this ISO timestamp."},
                        "before_timestamp": {"type": "string", "description": "Filter logs before this ISO timestamp."},
                        "component": {"type": "string", "description": "Filter logs by component name."}
                    }
                }
            }
        }
