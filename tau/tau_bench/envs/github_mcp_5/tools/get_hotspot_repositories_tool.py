# Copyright owned by Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetHotspotRepositoriesTool(Tool):
    """
    Identify hotspot repositories based on activity.

    This tool analyzes all repositories and ranks them based on activity, such as
    commit frequency, open pull requests, and unresolved alerts. It helps identify
    repositories requiring attention.

    Input Parameters:
        None

    Returns:
        str: JSON-formatted response containing:
            - status: "ok".
            - data: A list of repositories with their aggregated activity scores, including:
                - repo (str): Repository name.
                - activity_score (int): Deterministic numeric score based on activity.
                - report_date (str): Deterministic date stamp (CURRENT_DATE).

    Errors:
        - None. Returns an empty list if no repositories exist.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs: Any) -> str:
        issues = list(data.get("issues", {}).values())
        alerts = data.get("code_scanning_alerts", [])

        repo_hotspots = {}
        for i in issues:
            if i.get("state") == "open":
                repo_hotspots[i.get("repo")] = repo_hotspots.get(i.get("repo"), 0) + 1
        for a in alerts:
            if a.get("state") == "open":
                repo_hotspots[a.get("repo")] = repo_hotspots.get(a.get("repo"), 0) + 1

        result = [{"repo": r, "open_items": count, "report_date": CURRENT_DATE} for r, count in repo_hotspots.items()]
        return _response("ok", result)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_hotspot_repositories",
                "description": "Identify repositories with most open issues and alerts deterministically.",
                "parameters": {"type": "object", "properties": {}},
            },
        }
