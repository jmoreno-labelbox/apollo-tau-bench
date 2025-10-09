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



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetOpenSecurityAlertsTool(Tool):
    """
    Retrieve all open security alerts for a repository deterministically.

    This tool lists all code scanning alerts with state "open" for the given repository.
    Each alert is assigned a deterministic `alert_id` via `_safe_id`, severity is normalized
    to lowercase, and the result includes a `report_date`.

    Input Parameters:
        repo_name (str): The name of the repository.

    Returns:
        str: JSON-formatted response containing:
            - status: "ok" if alerts were found, or "error" otherwise.
            - data: A list of open alerts with metadata, including:
                - alert_id (str): Deterministic unique alert ID.
                - severity (str): Alert severity (normalized to lowercase).
                - state (str): The alert state ("open").
                - description (str): Alert description.
                - file (str): Affected file path.
                - branch (str): Branch where the issue was detected.
                - report_date (str): Deterministic date stamp (CURRENT_DATE).

    Errors:
        - Returns an error if `repo_name` is missing or invalid.
    """

    @staticmethod
    def invoke(data: dict[str, Any], repo_name: str) -> str:
        try:
            repo_name = _validate_param({"repo_name": repo_name}, "repo_name", str)
        except (ValueError, TypeError) as e:
            return _response("error", str(e), "VALIDATION_ERROR")

        alerts = data.get("code_scanning_alerts", [])
        repo_alerts = [
            {
                "alert_id": _safe_id(
                    a, "alert_id", f"ALERT_{repo_name}_", ["description", "file"]
                ),
                "severity": (a.get("severity") or "unknown").lower(),
                "state": a.get("state"),
                "description": a.get("description"),
                "file": a.get("file"),
                "branch": a.get("branch"),
                "report_date": CURRENT_DATE,
            }
            for a in alerts
            if a.get("repo") == repo_name and a.get("state") == "open"
        ]
        return _response("ok", repo_alerts)
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetOpenSecurityAlerts",
                "description": "List all open security alerts for a repository deterministically.",
                "parameters": {
                    "type": "object",
                    "properties": {"repo_name": {"type": "string"}},
                    "required": ["repo_name"],
                },
            },
        }
