# Sierra Copyright

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

def _normalize_user(user: Any) -> str:
    """
    Normalize user identifiers for deterministic outputs.

    Args:
        user (Any): Raw user field (string, int, or None).

    Returns:
        str: Stringified user identifier, or "unknown" if empty/None.
    """
    return str(user) if user else "unknown"

class GetPullRequestMetadataTool(Tool):
    """
    Retrieve deterministic metadata for a pull request by ID.

    This tool searches for a pull request by its deterministic ID (`pr_id`)
    and returns its metadata, augmented with a `report_date`.

    Input Parameters:
        repo_name (str): The name of the repository.
        pr_id (str): Deterministic ID of the pull request.

    Returns:
        str: JSON-formatted response containing:
            - status: "ok" if found, or "error" otherwise.
            - data: A dictionary with pull request metadata, including deterministic `pr_id`.

    Errors:
        - Returns an error if parameters are missing or invalid.
        - Returns an error if no pull request with the given ID exists.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs: Any) -> str:
        try:
            repo_name = _validate_param(kwargs, "repo_name", str)
            pr_number = _validate_param(kwargs, "pr_number", int)
        except (ValueError, TypeError) as e:
            return _response("error", str(e), "VALIDATION_ERROR")

        prs = list(data.get("pull_requests", {}).values())
        pr = next((p for p in prs if p.get("repo") == repo_name and p.get("number") == pr_number), None)

        if not pr:
            return _response("error", ERROR_MESSAGES["NOT_FOUND"].format(entity="Pull Request", entity_id=pr_number), "NOT_FOUND")

        result = {
            **pr,
            "pr_id": _safe_id(pr, "pr_id", f"PR_{repo_name}_", ["title", "head_branch", "base_branch"]),
            "report_date": CURRENT_DATE
        }
        if "author" in result:
            result["author"] = _normalize_user(result["author"])
        if "reviewers" in result:
            result["reviewers"] = [_normalize_user(r) for r in result.get("reviewers", [])]

        return _response("ok", result)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_pull_request_metadata",
                "description": "Retrieve deterministic metadata for a pull request by number.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_name": {"type": "string"},
                        "pr_number": {"type": "integer"},
                    },
                    "required": ["repo_name", "pr_number"],
                },
            },
        }