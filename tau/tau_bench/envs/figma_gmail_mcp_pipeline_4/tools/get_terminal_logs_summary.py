# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetTerminalLogsSummary(Tool):
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        """
        Retrieves terminal logs with filtering and summarization capabilities.
        """
        log_level = kwargs.get('log_level')
        source_component = kwargs.get('source_component')
        workflow_id = kwargs.get('workflow_id')
        message_keywords = kwargs.get('message_keywords', [])
        created_after = kwargs.get('created_after')
        created_before = kwargs.get('created_before')
        limit = kwargs.get('limit', 100)

        terminal_logs = data.get('terminal_logs', [])

        # Filter logs by criteria
        results = []
        for log in terminal_logs:
            # Apply filters
            if log_level:
                log_message = log.get('message', '')
                if not log_message.startswith(f"{log_level}:"):
                    continue

            if source_component:
                if log.get('component') != source_component:
                    continue

            if workflow_id:
                if log.get('workflow_id') != workflow_id:
                    continue

            if message_keywords:
                message = log.get('message', '').lower()
                if not any(keyword.lower() in message for keyword in message_keywords):
                    continue

            # Apply date filters
            if created_after:
                log_ts = log.get('log_ts', '')
                if log_ts < created_after:
                    continue

            if created_before:
                log_ts = log.get('log_ts', '')
                if log_ts > created_before:
                    continue

            results.append(log)

        # Sort by timestamp (most recent first) and apply limit
        results.sort(key=lambda x: x.get('log_ts', ''), reverse=True)
        if limit:
            results = results[:limit]

        # Create summary with log level distribution
        summary = {
            "total_matching_logs": len(results),
            "by_level": {},
            "by_component": {},
            "by_workflow": {},
            "logs": results
        }

        for log in results:
            # Extract log level from message
            message = log.get('message', '')
            level = 'UNKNOWN'
            for lvl in ['DEBUG', 'INFO', 'WARN', 'ERROR', 'CRITICAL']:
                if message.startswith(f"{lvl}:"):
                    level = lvl
                    break

            if level not in summary["by_level"]:
                summary["by_level"][level] = 0
            summary["by_level"][level] += 1

            # Group by component
            component = log.get('component', 'unknown')
            if component not in summary["by_component"]:
                summary["by_component"][component] = 0
            summary["by_component"][component] += 1

            # Group by workflow
            workflow = log.get('workflow_id', 'unknown')
            if workflow not in summary["by_workflow"]:
                summary["by_workflow"][workflow] = 0
            summary["by_workflow"][workflow] += 1

        return json.dumps(summary, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_terminal_logs_summary",
                "description": "Retrieves terminal logs with filtering and summarization capabilities including log level distribution, component breakdown, and workflow tracking.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "log_level": {"type": "string", "description": "Filter logs by level (e.g., 'INFO', 'ERROR', 'WARN')."},
                        "source_component": {"type": "string", "description": "Filter logs by source component or service."},
                        "workflow_id": {"type": "string", "description": "Filter logs by workflow ID."},
                        "message_keywords": {"type": "array", "items": {"type": "string"}, "description": "Filter logs by keywords in the message content."},
                        "created_after": {"type": "string", "description": "Filter logs created after this ISO timestamp."},
                        "created_before": {"type": "string", "description": "Filter logs created before this ISO timestamp."},
                        "limit": {"type": "integer", "description": "Maximum number of log entries to return (default: 100)."}
                    }
                }
            }
        }
