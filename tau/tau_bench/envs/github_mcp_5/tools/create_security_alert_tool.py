# Copyright Sierra

import hashlib
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

def _safe_id(obj: Dict[str, Any], explicit_id: str, fallback_prefix: str, fallback_fields: List[str]) -> str:
    """
    Generate a deterministic ID for an object, with robust fallback.

    Args:
        obj (Dict[str, Any]): The dictionary representing the entity.
        explicit_id (str): Key name for an existing ID in the object (e.g., "issue_id").
        fallback_prefix (str): Prefix for the ID (e.g., "ISSUE_", "PR_", "ALERT_").
        fallback_fields (List[str]): List of fields to build the ID seed (used in order).

    Returns:
        str: Deterministic ID string derived from existing ID, selected fields,
             or the full object JSON as fallback.
    """
    if obj.get(explicit_id):
        return obj[explicit_id]

    seed_parts = [str(obj.get(f, "")) for f in fallback_fields if obj.get(f)]
    seed = "_".join(seed_parts)

    if not seed:
        seed = json.dumps(obj, sort_keys=True)

    return f"{fallback_prefix}{hashlib.sha1(seed.encode()).hexdigest()[:8]}"

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
    def invoke(data: Dict[str, Any], ) -> str:
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