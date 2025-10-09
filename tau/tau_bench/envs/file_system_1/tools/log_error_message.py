from tau_bench.envs.tool import Tool
import json
from typing import Any



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class LogErrorMessage(Tool):
    """Generates a structured log of error messages for a failed task."""

    @staticmethod
    def invoke(
        data: dict[str, Any],
        error_type: str = None,
        task_type: str = None,
        task_id: str = None,
        user_id: str = None,
        severity: str = None,
        details_json: str = None
    ) -> str:
        error_logs = data.get("error_messages", [])
        new_id = f"err_msg_{max((int(e['msg_id'].split('_')[-1]) for e in error_logs), default=0) + 1:03d}"

        # Automatically create a message according to the error type and task specifics
        # Create a suitable message depending on the error type
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
            "msg_id": new_id,
            "err_type": error_type,
            "task_id": task_id,
            "task_type": task_type,
            "user_id": user_id,
            "msg": message,
            "created_at": "2024-01-20T12:00:00Z",
            "severity": severity,
            "details": details_json,
        }
        error_logs.append(new_log)
        data["error_messages"] = error_logs
        payload = new_log
        out = json.dumps(payload)
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "LogErrorMessage",
                "description": "Logs a structured error message for auditing and alerting purposes.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "task_id": {"type": "string"},
                        "task_type": {"type": "string"},
                        "user_id": {"type": "string"},
                        "error_type": {"type": "string"},
                        "severity": {
                            "type": "string",
                            "enum": ["low", "medium", "high", "critical"],
                        },
                        "details_json": {"type": "object"},
                    },
                    "required": [
                        "task_id",
                        "task_type",
                        "user_id",
                        "error_type",
                        "severity",
                    ],
                },
            },
        }
