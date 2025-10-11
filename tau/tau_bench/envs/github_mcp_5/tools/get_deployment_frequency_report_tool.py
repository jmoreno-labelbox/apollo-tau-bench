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

class GetDeploymentFrequencyReportTool(Tool):
    """
    Generate a deterministic deployment frequency report.

    This tool calculates the number of deploy events for a repository within a
    deterministic time window (e.g., daily, weekly, monthly). It provides insights
    into how frequently deployments occur in different environments.

    Input Parameters:
        repo_name (str): The name of the repository.
        period (str): The aggregation period for frequency ("daily", "weekly", "monthly").

    Returns:
        str: JSON-formatted response containing:
            - status: "ok" if calculated successfully, or "error" otherwise.
            - data: A dictionary with:
                - repo (str): The repository name.
                - period (str): The selected aggregation period.
                - deploy_counts (Dict[str, int]): Number of deploys per environment.
                - report_date (str): Deterministic date stamp (CURRENT_DATE).

    Errors:
        - Returns an error if `repo_name` or `period` is missing or invalid.
        - Returns an error if no deploy events exist for the repository.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], ) -> str:
        try:
            repo_name = _validate_param(kwargs, "repo_name", str)
        except (ValueError, TypeError) as e:
            return _response("error", str(e), "VALIDATION_ERROR")

        events = data.get("terminal", [])
        deploys = [d for d in events if d.get("repo") == repo_name and d.get("type") == "deploy"]
        deploys = sorted(deploys, key=lambda d: (d.get("date"), d.get("event_id")))


        deploy_dates = sorted([d.get("date") for d in deploys if d.get("date")])

        intervals = []
        for i in range(1, len(deploy_dates)):
            intervals.append(_days_between(deploy_dates[i - 1], deploy_dates[i]))

        average_interval = int(sum(intervals) / len(intervals)) if intervals else 0

        report = {
            "repo": repo_name,
            "deploy_count": len(deploys),
            "average_interval_days": average_interval,
            "deploy_events": [
                {"event_id": d["event_id"], "date": d["date"], "environment": d["environment"]}
                for d in deploys
            ],
            "report_date": CURRENT_DATE,
        }
        return _response("ok", report)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_deployment_frequency_report",
                "description": "Get deterministic deployment frequency stats for a repository.",
                "parameters": {
                    "type": "object",
                    "properties": {"repo_name": {"type": "string"}},
                    "required": ["repo_name"],
                },
            },
        }