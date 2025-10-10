# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class LogErrorMessage(Tool):
    """Creates a structured error message log for a failed task."""
    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        error_logs = data.get('error_messages', [])
        new_id = f"err_msg_{max((int(e['msg_id'].split('_')[-1]) for e in error_logs), default=0) + 1:03d}"

        # Automatically generate message based on error type and task details
        error_type = kwargs.get("error_type")
        task_type = kwargs.get("task_type")
        task_id = kwargs.get("task_id")

        # Generate appropriate message based on error type
        if error_type == "permission_denied":
            message = f"Permission denied while executing {task_type} task {task_id}"
        elif error_type == "file_not_found":
            message = f"Required file not found during {task_type} task {task_id}"
        elif error_type == "network_error":
            message = f"Network connection failed during {task_type} task {task_id}"
        elif error_type == "timeout":
            message = f"Operation timed out during {task_type} task {task_id}"
        elif error_type == "validation_failed":
            message = f"Data validation failed for {task_type} task {task_id}"
        else:
            message = f"Error occurred during {task_type} task {task_id}: {error_type}"

        new_log = {
            "msg_id": new_id, "err_type": error_type, "task_id": task_id, "task_type": task_type, "user_id": kwargs.get("user_id"), "msg": message, "created_at": "2024-01-20T12:00:00Z", "severity": kwargs.get("severity"), "details": kwargs.get("details_json")}
        error_logs.append(new_log)
        data['error_messages'] = error_logs
        return json.dumps(new_log)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {"type": "function", "function": {"name": "log_error_message", "description": "Logs a structured error message for auditing and alerting purposes.", "parameters": {"type": "object", "properties": {"task_id": {"type": "string"}, "task_type": {"type": "string"}, "user_id": {"type": "string"}, "error_type": {"type": "string"}, "severity": {"type": "string", "enum": ["low", "medium", "high", "critical"]}, "details_json": {"type": "object"}}, "required": ["task_id", "task_type", "user_id", "error_type", "severity"]}}}
