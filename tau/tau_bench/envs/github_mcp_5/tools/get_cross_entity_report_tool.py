# Copyright © Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


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
