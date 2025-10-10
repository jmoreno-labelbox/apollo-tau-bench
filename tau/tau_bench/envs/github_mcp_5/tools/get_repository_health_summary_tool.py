# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetRepositoryHealthSummaryTool(Tool):
    """
    Aggregate repository health metrics (issues, PRs, alerts).

    This tool generates a deterministic summary of the health of a repository,
    based on the number of open issues, open pull requests, and open security alerts.
    It provides a quick overview of repository status with an added deterministic
    `report_date` field.

    Usage:
        - Provide the repository name.
        - Returns aggregated counts of open issues, pull requests, and alerts.

    Input Parameters:
        repo_name (str): The unique name of the repository to summarize.

    Returns:
        str: JSON-formatted response containing:
            - status: "ok" if successful, or "error" otherwise.
            - data: A dictionary with the following keys:
                - repo (str): The repository name.
                - open_issues (int): Number of open issues.
                - open_prs (int): Number of open pull requests.
                - open_alerts (int): Number of open security alerts.
                - report_date (str): Deterministic date stamp (CURRENT_DATE).

    Errors:
        - Returns an error if `repo_name` is missing or of the wrong type.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs: Any) -> str:
        try:
            repo_name = _validate_param(kwargs, "repo_name", str)
        except (ValueError, TypeError) as e:
            return _response("error", str(e), "VALIDATION_ERROR")

        issues = list(data.get("issues", {}).values())
        prs = list(data.get("pull_requests", {}).values())
        alerts = data.get("code_scanning_alerts", [])

        result = {
            "repo": repo_name,
            "open_issues": sum(1 for i in issues if i.get("repo") == repo_name and i.get("state") == "open"),
            "open_prs": sum(1 for p in prs if p.get("repo") == repo_name and p.get("state") == "open"),
            "open_alerts": sum(1 for a in alerts if a.get("repo") == repo_name and a.get("state") == "open"),
            "report_date": CURRENT_DATE,
        }
        return _response("ok", result)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_repository_health_summary",
                "description": "Get a deterministic repository health summary (issues, PRs, alerts).",
                "parameters": {
                    "type": "object",
                    "properties": {"repo_name": {"type": "string"}},
                    "required": ["repo_name"],
                },
            },
        }
