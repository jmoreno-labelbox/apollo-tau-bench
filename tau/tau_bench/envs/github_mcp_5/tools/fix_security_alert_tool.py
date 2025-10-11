# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool






def _validate_param(
    kwargs: Dict[str, Any],
    param: str,
    expected_type: type,
    required: bool = True,
    subtype: type = None
) -> Any:
    """
    Validate and retrieve a parameter from keyword arguments.

    Performs deterministic validation on the presence and type of a parameter,
    with optional subtype checks when the parameter is a list.

    Args:
        kwargs (Dict[str, Any]): Dictionary of keyword arguments to validate.
        param (str): The name of the parameter to validate.
        expected_type (type): Expected top-level type of the parameter (e.g., str, list).
        required (bool, optional): Whether the parameter is required. Defaults to True.
        subtype (type, optional): Expected element type if the parameter is a list.
            For example, subtype=str enforces that all elements in the list are strings.

    Returns:
        Any: The validated parameter value if present and valid, or None if not required.
             On validation failure, returns a standardized error response.
    """
    value = kwargs.get(param)

    if required and value is None:
        return _response(
            "error",
            ERROR_MESSAGES["REQUIRED_PARAMETER"].format(param=param)
        )

    if value is not None and not isinstance(value, expected_type):
        return _response(
            "error",
            ERROR_MESSAGES["INVALID_PARAMETER_TYPE"].format(
                param=param,
                expected_type=expected_type.__name__
            )
        )

    if subtype and isinstance(value, list):
        for item in value:
            if not isinstance(item, subtype):
                return _response(
                    "error",
                    f"Parameter '{param}' must be a list of {subtype.__name__}."
                )

    return value

def _response(status: str, data_or_message: Any, error_code: str = None) -> str:
    """
    Build a standardized JSON response.

    Args:
        status (str): Response status, either "ok" or "error".
        data_or_message (Any): Data payload when status is "ok", or error message when status is "error".
        error_code (str, optional): Machine-friendly error code to include when status is "error".

    Returns:
        str: A JSON-formatted string containing either:
             {"status": "ok", "data": ...}
             or {"status": "error", "error_code": ..., "message": ...},
             indented for readability.
    """
    if status == "ok":
        return json.dumps({"status": "ok", "data": data_or_message}, indent=2)
    return json.dumps(
        {
            "status": "error",
            "error_code": error_code or "UNKNOWN_ERROR",
            "message": data_or_message,
        },
        indent=2,
    )

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
    def invoke(data: Dict[str, Any], ) -> str:
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