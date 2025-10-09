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
        return list(db)
    return db

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
    def invoke(data: dict[str, Any], repo_name: str) -> str:
        try:
            repo_name = _validate_param({"repo_name": repo_name}, "repo_name", str)
        except (ValueError, TypeError) as e:
            return _response("error", str(e), "VALIDATION_ERROR")

        issues = data.get("issues", {}).values()
        prs = data.get("pull_requests", {}).values()
        alerts = data.get("code_scanning_alerts", {}).values()

        result = {
            "repo": repo_name,
            "open_issues": sum(
                1
                for i in issues.values() if i.get("repo") == repo_name and i.get("state") == "open"
            ),
            "open_prs": sum(
                1
                for p in prs.values() if p.get("repo") == repo_name and p.get("state") == "open"
            ),
            "open_alerts": sum(
                1
                for a in alerts.values() if a.get("repo") == repo_name and a.get("state") == "open"
            ),
            "report_date": CURRENT_DATE,
        }
        return _response("ok", result)
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetRepositoryHealthSummary",
                "description": "Get a deterministic repository health summary (issues, PRs, alerts).",
                "parameters": {
                    "type": "object",
                    "properties": {"repo_name": {"type": "string"}},
                    "required": ["repo_name"],
                },
            },
        }
