# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class CreateSecurityAlertTool(Tool):
    """
    Create a new security alert deterministically (in-memory only).

    This tool simulates the creation of a new code scanning alert in a repository.
    IDs are generated with `_safe_id` using description and file. Severity is
    normalized to lowercase, and metadata is stamped with CURRENT_DATE.

    Input Parameters:
        repo_name (str): The name of the repository.
        description (str): Description of the security issue.
        file (str): The file path affected by the issue.
        branch (str): The branch where the issue was found.
        severity (str): Severity of the alert (e.g., "low", "medium", "high").

    Returns:
        str: JSON-formatted response containing:
            - status: "ok" if created successfully, or "error" otherwise.
            - data: Metadata of the created security alert, including deterministic `alert_id`.

    Errors:
        - Returns an error if required parameters are missing or invalid.
        - Returns an error if a similar alert already exists in the repository.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs: Any) -> str:
        try:
            repo_name = _validate_param(kwargs, "repo_name", str)
            severity = _validate_param(kwargs, "severity", str)
            description = _validate_param(kwargs, "description", str)
            file = _validate_param(kwargs, "file", str)
            branch = _validate_param(kwargs, "branch", str)
        except (ValueError, TypeError) as e:
            return _response("error", str(e), "VALIDATION_ERROR")

        alerts = data.get("code_scanning_alerts", [])
        if any(a.get("repo") == repo_name and a.get("description") == description for a in alerts):
            return _response("error", ERROR_MESSAGES["ALREADY_EXISTS"].format(entity="SecurityAlert", entity_id=description), "ALREADY_EXISTS")

        new_number = len(alerts) + 1
        new_alert = {
            "repo": repo_name,
            "number": new_number,
            "severity": severity,
            "state": "open",
            "description": description,
            "file": file,
            "branch": branch,
            "created_at": CURRENT_DATE,
            "updated_at": CURRENT_DATE,
        }
        new_alert["alert_id"] = _safe_id(new_alert, "alert_id", f"ALERT_{repo_name}_", ["description", "file"])
        alerts.append(new_alert)
        return _response("ok", new_alert)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "create_security_alert",
                "description": "Create a new deterministic security alert (in-memory only).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_name": {"type": "string"},
                        "severity": {"type": "string"},
                        "description": {"type": "string"},
                        "file": {"type": "string"},
                        "branch": {"type": "string"},
                    },
                    "required": ["repo_name", "severity", "description", "file", "branch"],
                },
            },
        }
