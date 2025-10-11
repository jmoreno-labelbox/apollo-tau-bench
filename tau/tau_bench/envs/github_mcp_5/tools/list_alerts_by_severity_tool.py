# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class ListAlertsBySeverityTool(Tool):
    """
    List security alerts for a repository filtered by severity.

    This tool retrieves all alerts for a repository with a given severity level.
    Severity values are normalized to lowercase for deterministic filtering.
    Each alert is returned with a deterministic `alert_id` via `_safe_id`.

    Input Parameters:
        repo_name (str): The name of the repository.
        severity (str): Severity level to filter by (e.g., "low", "medium", "high").

    Returns:
        str: JSON-formatted response containing:
            - status: "ok" if alerts were found, or "error" otherwise.
            - data: A list of alerts with metadata, including:
                - alert_id (str): Deterministic unique alert ID.
                - severity (str): Normalized severity.
                - state (str): Current state of the alert.
                - description (str): Alert description.
                - file (str): Affected file.
                - branch (str): Branch where the issue was detected.
                - report_date (str): Deterministic date stamp (CURRENT_DATE).

    Errors:
        - Returns an error if parameters are missing or invalid.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs: Any) -> str:
        try:
            repo_name = _validate_param(kwargs, "repo_name", str)
            severity = _validate_param(kwargs, "severity", str)
        except (ValueError, TypeError) as e:
            return _response("error", str(e), "VALIDATION_ERROR")

        alerts = data.get("code_scanning_alerts", [])
        filtered = [
            {
                "alert_id": _safe_id(a, "alert_id", f"ALERT_{repo_name}_", ["description", "file"]),
                "severity": (a.get("severity") or "unknown").lower(),
                "state": a.get("state"),
                "description": a.get("description"),
                "report_date": CURRENT_DATE,
            }
            for a in alerts
            if a.get("repo") == repo_name and (a.get("severity") or "").lower() == severity.lower()
        ]
        return _response("ok", filtered)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_alerts_by_severity",
                "description": "List security alerts for a repository filtered by severity.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_name": {"type": "string"},
                        "severity": {"type": "string"},
                    },
                    "required": ["repo_name", "severity"],
                },
            },
        }
