# Copyright Sierra

import datetime
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

def _days_between(start: str, end: str) -> int:
    """
    Calculate the absolute number of days between two date strings.

    Supports flexible parsing (YYYY-MM-DD, YYYY/MM/DD).
    Returns 0 if parsing fails.

    Args:
        start (str): Start date string.
        end (str): End date string.

    Returns:
        int: Absolute difference in days, or 0 on error.
    """
    if not isinstance(start, str) or not isinstance(end, str):
        return 0

    formats = ["%Y-%m-%d", "%Y/%m/%d"]
    for fmt in formats:
        try:
            start_dt = datetime.strptime(start, fmt)
            end_dt = datetime.strptime(end, fmt)
            return abs((end_dt - start_dt).days)
        except ValueError:
            continue
    return 0

class GetCrossEntityReportTool(Tool):
    """
    Generate a deterministic cross-entity report consolidating issues, PRs, commits, alerts, and deployments.

    This tool links entities (Issues ↔ PRs ↔ Commits ↔ Alerts ↔ Deploys) into a single summary.

    Input Parameters:
        repo_name (str): The repository name.

    Returns:
        str: JSON response containing:
            - status: "ok"
            - data: {
                "repo": str,
                "open_issues": int,
                "merged_prs": int,
                "recent_commits": int (last 30 days),
                "open_alerts": int,
                "last_deployment": str,
                "report_date": str
            }
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs: Any) -> str:
        repo_name = _validate_param(kwargs, "repo_name", str)

        issues = list(data.get("issues", {}).values())
        prs = list(data.get("pull_requests", {}).values())
        commits = list(data.get("commits", {}).values())
        alerts = data.get("code_scanning_alerts", [])
        deploys = list(data.get("deployments", {}).values())

        result = {
            "repo": repo_name,
            "open_issues": sum(1 for i in issues if i.get("repo") == repo_name and i.get("state") == "open"),
            "merged_prs": sum(1 for p in prs if p.get("repo") == repo_name and p.get("state") == "merged"),
            "recent_commits": sum(1 for c in commits if c.get("repo") == repo_name and _days_between(c.get("timestamp", CURRENT_DATE), CURRENT_DATE) <= 30),
            "open_alerts": sum(1 for a in alerts if a.get("repo") == repo_name and a.get("state") == "open"),
            "last_deployment": max(
                (d.get("deployment_date") for d in deploys if d.get("repo") == repo_name),
                default="none"
            ),
            "report_date": CURRENT_DATE,
        }
        return _response("ok", result)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_cross_entity_report",
                "description": "Generate deterministic cross-entity report (issues, PRs, commits, alerts, deploys).",
                "parameters": {
                    "type": "object",
                    "properties": {"repo_name": {"type": "string"}},
                    "required": ["repo_name"],
                },
            },
        }