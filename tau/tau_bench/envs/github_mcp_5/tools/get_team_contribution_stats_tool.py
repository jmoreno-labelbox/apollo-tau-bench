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

class GetTeamContributionStatsTool(Tool):
    """
    Generate deterministic contribution statistics for a team.

    This tool aggregates commit, pull request, and issue contributions across a repository,
    grouped by team members. Author identifiers are normalized via `_normalize_user`.
    Labels and severity values are normalized for consistency.

    Input Parameters:
        repo_name (str): The name of the repository.

    Returns:
        str: JSON-formatted response containing:
            - status: "ok" if successful.
            - data: Contribution statistics, including:
                - commits_by_author (Dict[str, int]): Commits per author.
                - prs_by_author (Dict[str, int]): Pull requests per author.
                - issues_by_author (Dict[str, int]): Issues created per author.
                - report_date (str): Deterministic date stamp (CURRENT_DATE).

    Errors:
        - Returns an error if `repo_name` is missing or invalid.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], ) -> str:
        repo_name = _validate_param(kwargs, "repo_name", str)

        commits = list(data.get("commits", {}).values())
        prs = list(data.get("pull_requests", {}).values())
        issues = list(data.get("issues", {}).values())

        stats = {}
        for c in commits:
            if c.get("repo") == repo_name:
                author = _normalize_user(c.get("author"))
                stats.setdefault(author, {"commits": 0, "prs": 0, "issues": 0})
                stats[author]["commits"] += 1
        for p in prs:
            if p.get("repo") == repo_name:
                author = _normalize_user(p.get("author"))
                stats.setdefault(author, {"commits": 0, "prs": 0, "issues": 0})
                stats[author]["prs"] += 1
        for i in issues:
            if i.get("repo") == repo_name:
                for a in [_normalize_user(a) for a in i.get("assignees", [])]:
                    stats.setdefault(a, {"commits": 0, "prs": 0, "issues": 0})
                    stats[a]["issues"] += 1

        result = {"repo": repo_name, "team_stats": stats, "report_date": CURRENT_DATE}
        return _response("ok", result)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_team_contribution_stats",
                "description": "Calculate contributions (commits, PRs, issues) per user deterministically.",
                "parameters": {
                    "type": "object",
                    "properties": {"repo_name": {"type": "string"}},
                    "required": ["repo_name"],
                },
            },
        }