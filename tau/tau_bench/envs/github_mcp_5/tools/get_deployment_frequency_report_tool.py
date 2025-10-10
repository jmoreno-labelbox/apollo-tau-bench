# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


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
    def invoke(data: Dict[str, Any], **kwargs: Any) -> str:
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
