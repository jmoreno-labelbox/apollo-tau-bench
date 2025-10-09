from tau_bench.envs.tool import Tool
import calendar
import json
import os
import random
import uuid
from datetime import datetime, timezone
from typing import Any
import hashlib
from datetime import datetime



def _convert_db_to_list(db):
    """Convert database from dict format to list format."""
    if isinstance(db, dict):
        return list(db.values())
    return db

class GetRepositoryActivityDashboardTool(Tool):
    """
    Generate a deterministic activity dashboard for a repository.

    This tool aggregates key activity metrics for a repository, including commits,
    pull requests, issues, and alerts. It provides a holistic view of repository health
    and activity trends, normalized for deterministic outputs.

    Input Parameters:
        repo_name (str): The name of the repository.

    Returns:
        str: JSON-formatted response containing:
            - status: "ok" if successful.
            - data: A dictionary with aggregated metrics:
                - total_commits (int): Total commits in the repository.
                - open_prs (int): Number of open pull requests.
                - merged_prs (int): Number of merged pull requests.
                - open_issues (int): Number of open issues.
                - closed_issues (int): Number of closed issues.
                - open_alerts (int): Number of open security alerts.
                - report_date (str): Deterministic date stamp (CURRENT_DATE).

    Errors:
        - Returns an error if `repo_name` is missing or invalid.
    """

    @staticmethod
    def invoke(data: dict[str, Any], repo_name: str) -> str:
        pass
        try:
            repo_name = _validate_param({"repo_name": repo_name}, "repo_name", str)
        except (ValueError, TypeError) as e:
            return _response("error", str(e), "VALIDATION_ERROR")

        commits = data.get("commits", [])
        issues = data.get("issues", [])
        prs = data.get("pull_requests", [])
        alerts = data.get("code_scanning_alerts", [])

        dashboard = {
            "repo": repo_name,
            "commits_count": sum(1 for c in commits if c.get("repo") == repo_name),
            "open_issues": sum(
                1
                for i in issues
                if i.get("repo") == repo_name and i.get("state") == "open"
            ),
            "open_prs": sum(
                1
                for p in prs
                if p.get("repo") == repo_name and p.get("state") == "open"
            ),
            "open_alerts_by_severity": {
                sev: sum(
                    1
                    for a in alerts
                    if a.get("repo") == repo_name
                    and a.get("state") == "open"
                    and (a.get("severity") or "unknown").lower() == sev
                )
                for sev in ["critical", "high", "medium", "low", "unknown"]
            },
            "open_alerts": sum(
                1
                for a in alerts
                if a.get("repo") == repo_name and a.get("state") == "open"
            ),
            "report_date": CURRENT_DATE,
        }
        return _response("ok", dashboard)
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetRepositoryActivityDashboard",
                "description": "Summarize repository activity (commits, issues, PRs, alerts).",
                "parameters": {
                    "type": "object",
                    "properties": {"repo_name": {"type": "string"}},
                    "required": ["repo_name"],
                },
            },
        }
