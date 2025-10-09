from tau_bench.envs.tool import Tool
import json
import uuid
from datetime import datetime
from typing import Any

class GetTerminalLogsSummary(Tool):
    @staticmethod
    def invoke(
        data: dict[str, Any],
        log_level: str = None,
        source_component: str = None,
        component: str = None,
        workflow_id: str = None,
        message_keywords: list[str] = [],
        created_after: str = None,
        created_before: str = None,
        limit: int = 100
    ) -> str:
        # Support 'component' as an alternative to 'source_component'
        if component is not None:
            source_component = component
        """
        Obtains terminal logs with filtering and summarization features.
        """
        terminal_logs = data.get("terminal_logs", [])

        # Sort logs based on specified criteria
        results = []
        for log in terminal_logs:
            # Implement filters
            if log_level:
                log_message = log.get("message", "")
                if not log_message.startswith(f"{log_level}:"):
                    continue

            if source_component:
                if log.get("component") != source_component:
                    continue

            if workflow_id:
                if log.get("workflow_id") != workflow_id:
                    continue

            if message_keywords:
                message = log.get("message", "").lower()
                if not any(keyword.lower() in message for keyword in message_keywords):
                    continue

            # Enforce date filters
            if created_after:
                log_ts = log.get("log_ts", "")
                if log_ts < created_after:
                    continue

            if created_before:
                log_ts = log.get("log_ts", "")
                if log_ts > created_before:
                    continue

            results.append(log)

        # Order by timestamp (latest first) and enforce limit
        results.sort(key=lambda x: x.get("log_ts", ""), reverse=True)
        if limit:
            results = results[:limit]

        # Generate a summary showing log level distribution
        summary = {
            "total_matching_logs": len(results),
            "by_level": {},
            "by_component": {},
            "by_workflow": {},
            "logs": results,
        }

        for log in results:
            # Retrieve log level from the message
            message = log.get("message", "")
            level = "UNKNOWN"
            for lvl in ["DEBUG", "INFO", "WARN", "ERROR", "CRITICAL"]:
                if message.startswith(f"{lvl}:"):
                    level = lvl
                    break

            if level not in summary["by_level"]:
                summary["by_level"][level] = 0
            summary["by_level"][level] += 1

            # Categorize by component
            component = log.get("component", "unknown")
            if component not in summary["by_component"]:
                summary["by_component"][component] = 0
            summary["by_component"][component] += 1

            # Classify by workflow
            workflow = log.get("workflow_id", "unknown")
            if workflow not in summary["by_workflow"]:
                summary["by_workflow"][workflow] = 0
            summary["by_workflow"][workflow] += 1
        payload = summary
        out = json.dumps(payload, indent=2)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetTerminalLogsSummary",
                "description": "Retrieves terminal logs with filtering and summarization capabilities including log level distribution, component breakdown, and workflow tracking.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "log_level": {
                            "type": "string",
                            "description": "Filter logs by level (e.g., 'INFO', 'ERROR', 'WARN').",
                        },
                        "source_component": {
                            "type": "string",
                            "description": "Filter logs by source component or service.",
                        },
                        "workflow_id": {
                            "type": "string",
                            "description": "Filter logs by workflow ID.",
                        },
                        "message_keywords": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Filter logs by keywords in the message content.",
                        },
                        "created_after": {
                            "type": "string",
                            "description": "Filter logs created after this ISO timestamp.",
                        },
                        "created_before": {
                            "type": "string",
                            "description": "Filter logs created before this ISO timestamp.",
                        },
                        "limit": {
                            "type": "integer",
                            "description": "Maximum number of log entries to return (default: 100).",
                        },
                    },
                },
            },
        }
