# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GenerateEndToEndReportTool(Tool):
    """
    Generate a deterministic end-to-end report for a repository.

    This tool consolidates multiple aspects of repository health into a single
    comprehensive report, including commits, pull requests, issues, alerts,
    releases, and deploy events. It is intended as a holistic snapshot
    for governance and auditing.

    Input Parameters:
        repo_name (str): The name of the repository.

    Returns:
        str: JSON-formatted response containing:
            - status: "ok" if successful.
            - data: Comprehensive repository report, including:
                - repo (str): Repository name.
                - commit_stats (Dict): Commit activity metrics.
                - pr_stats (Dict): Pull request activity metrics.
                - issue_stats (Dict): Issue activity metrics.
                - alert_stats (Dict): Security alert metrics.
                - release_info (Dict): Latest release metadata.
                - deploy_stats (Dict): Deployment frequency or events.
                - report_date (str): Deterministic date stamp (CURRENT_DATE).

    Errors:
        - Returns an error if `repo_name` is missing or invalid.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs: Any) -> str:
        repo_name = _validate_param(kwargs, "repo_name", str)

        commits = list(data.get("commits", {}).values())
        issues = list(data.get("issues", {}).values())
        prs = list(data.get("pull_requests", {}).values())
        alerts = data.get("code_scanning_alerts", [])
        releases = data.get("releases", [])

        report = {
            "repo": repo_name,
            "commits_count": sum(1 for c in commits if c.get("repo") == repo_name),
            "open_issues": sum(1 for i in issues if i.get("repo") == repo_name and i.get("state") == "open"),
            "merged_prs": sum(1 for p in prs if p.get("repo") == repo_name and p.get("state") == "merged"),
            "open_alerts": sum(1 for a in alerts if a.get("repo") == repo_name and a.get("state") == "open"),
            "releases_count": sum(1 for r in releases if r.get("repo") == repo_name),
            "report_date": CURRENT_DATE,
        }
        return _response("ok", report)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "generate_end_to_end_report",
                "description": "Generate deterministic end-to-end report (issues, PRs, commits, alerts, releases).",
                "parameters": {
                    "type": "object",
                    "properties": {"repo_name": {"type": "string"}},
                    "required": ["repo_name"],
                },
            },
        }
