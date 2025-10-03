from tau_bench.envs.tool import Tool
import calendar
import json
import os
import random
import uuid
from datetime import datetime, timezone
from typing import Any
import hashlib
from datetime import datetime

class GetResolvedSecurityAlertsTool(Tool):
    """
    Retrieve all resolved security alerts for a repository deterministically.

    This tool lists all code scanning alerts with state "resolved" for the given repository.
    Each alert is assigned a deterministic `alert_id` via `_safe_id`, severity is normalized
    to lowercase, and the result includes a `report_date`. If `resolved_at` is missing,
    it is set to CURRENT_DATE.

    Input Parameters:
        repo_name (str): The name of the repository.

    Returns:
        str: JSON-formatted response containing:
            - status: "ok" if alerts were found, or "error" otherwise.
            - data: A list of resolved alerts with metadata, including:
                - alert_id (str): Deterministic unique alert ID.
                - severity (str): Alert severity (normalized to lowercase).
                - state (str): The alert state ("resolved").
                - description (str): Alert description.
                - file (str): Affected file path.
                - branch (str): Branch where the issue was detected.
                - resolved_at (str): Resolution timestamp (existing or CURRENT_DATE).
                - report_date (str): Deterministic date stamp (CURRENT_DATE).

    Errors:
        - Returns an error if `repo_name` is missing or invalid.
    """

    @staticmethod
    def invoke(data: dict[str, Any], repo_name: str) -> str:
        pass
        try:
            repo_name = _validate_param({"repo_name": repo_name}, "repo_name", str)
        except (ValueError, TypeError) as e:
            return _response("error", str(e), "VALIDATION_ERROR")

        alerts = data.get("code_scanning_alerts", [])
        resolved = [
            {
                "alert_id": _safe_id(
                    a, "alert_id", f"ALERT_{repo_name}_", ["description", "file"]
                ),
                "severity": (a.get("severity") or "unknown").lower(),
                "state": a.get("state"),
                "resolved_at": a.get("resolved_at") or CURRENT_DATE,
                "description": a.get("description"),
            }
            for a in alerts
            if a.get("repo") == repo_name and a.get("state") in ["fixed", "dismissed"]
        ]
        return _response("ok", resolved)
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetResolvedSecurityAlerts",
                "description": "List all resolved security alerts for a repository deterministically.",
                "parameters": {
                    "type": "object",
                    "properties": {"repo_name": {"type": "string"}},
                    "required": ["repo_name"],
                },
            },
        }
