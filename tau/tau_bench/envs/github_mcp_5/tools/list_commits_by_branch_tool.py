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

def _normalize_user(user: Any) -> str:
    """
    Normalize user identifiers for deterministic outputs.

    Args:
        user (Any): Raw user field (string, int, or None).

    Returns:
        str: Stringified user identifier, or "unknown" if empty/None.
    """
    return str(user) if user else "unknown"

class ListCommitsByBranchTool(Tool):
    """
    List commits for a repository branch deterministically.

    This tool retrieves all commits for a given repository branch and augments
    each commit with a deterministic `report_date` field. Author fields are
    normalized with `_normalize_user` to ensure consistent outputs.

    Usage:
        - Provide the repository name and branch name.
        - Returns metadata for all commits matching that repository and branch.

    Input Parameters:
        repo_name (str): The name of the repository.
        branch (str): The branch name within the repository.

    Returns:
        str: JSON-formatted response containing:
            - status: "ok" if successful, or "error" otherwise.
            - data: A list of commits, each represented as a dictionary with:
                - commit_id (str): The commit SHA identifier.
                - repo (str): The repository name.
                - branch (str): The branch name.
                - message (str): The commit message.
                - author (str): The normalized author identifier.
                - timestamp (str): The commit timestamp.
                - report_date (str): Deterministic date stamp (CURRENT_DATE).

    Errors:
        - Returns an error if `repo_name` or `branch` are missing or of the wrong type.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], ) -> str:
        try:
            repo_name = _validate_param(kwargs, "repo_name", str)
            branch = _validate_param(kwargs, "branch", str)
        except (ValueError, TypeError) as e:
            return _response("error", str(e), "VALIDATION_ERROR")

        commits = list(data.get("commits", {}).values())
        branch_commits = [
            {
                "commit_id": c.get("sha"),
                "repo": repo_name,
                "branch": branch,
                "message": c.get("message"),
                "author": _normalize_user(c.get("author")),
                "timestamp": c.get("timestamp"),
                "report_date": CURRENT_DATE,
            }
            for c in commits
            if c.get("repo") == repo_name and c.get("branch") == branch
        ]
        return _response("ok", branch_commits)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "list_commits_by_branch",
                "description": "List commits for a repository branch deterministically.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "repo_name": {"type": "string"},
                        "branch": {"type": "string"},
                    },
                    "required": ["repo_name", "branch"],
                },
            },
        }