# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class FixSecurityAlertTool(Tool):
    """
    Mark an existing security alert as resolved (in-memory only).

    This tool updates the state of an alert from "open" to "resolved".
    The `resolved_at` and `updated_at` timestamps are set deterministically
    to CURRENT_DATE if not already present.

    Input Parameters:
        repo_name (str): The name of the repository.
        alert_id (str): Deterministic ID of the security alert to resolve.

    Returns:
        str: JSON-formatted response containing:
            - status: "ok" if the alert was resolved successfully, or "error" otherwise.
            - data: Updated alert metadata, including state, `resolved_at`, and `updated_at`.

    Errors:
        - Returns an error if parameters are missing or invalid.
        - Returns an error if the alert does not exist in the repository.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs: Any) -> str:
        try:
            repo_name = _validate_param(kwargs, "repo_name", str)
            alert_number = _validate_param(kwargs, "alert_number", int)
        except (ValueError, TypeError) as e:
            return _response("error", str(e), "VALIDATION_ERROR")

        alerts = data.get("code_scanning_alerts", [])
        alert = next((a for a in alerts if a.get("repo") == repo_name and a.get("number") == alert_number), None)

        if not alert:
            return _response("error", ERROR_MESSAGES["NOT_FOUND"].format(entity="Alert", entity_id=alert_number), "NOT_FOUND")

        alert["state"] = "fixed"
        alert["resolved_at"] = CURRENT_DATE
        alert["updated_at"] = CURRENT_DATE
        return _response("ok", alert)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "fix_security_alert",
                "description": "Mark a security alert as fixed deterministically.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_name": {"type": "string"},
                        "alert_number": {"type": "integer"},
                    },
                    "required": ["repo_name", "alert_number"],
                },
            },
        }
