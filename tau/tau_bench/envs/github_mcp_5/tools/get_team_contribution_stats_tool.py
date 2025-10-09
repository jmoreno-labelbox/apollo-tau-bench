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
    def invoke(data: dict[str, Any], repo_name: str) -> str:
        commits = data.get("commits", {}).values()
        prs = data.get("pull_requests", {}).values()
        issues = data.get("issues", {}).values()

        stats = {}
        for c in commits.values():
            if c.get("repo") == repo_name:
                author = _normalize_user(c.get("author"))
                stats.setdefault(author, {"commits": 0, "prs": 0, "issues": 0})
                stats[author]["commits"] += 1
        for p in prs.values():
            if p.get("repo") == repo_name:
                author = _normalize_user(p.get("author"))
                stats.setdefault(author, {"commits": 0, "prs": 0, "issues": 0})
                stats[author]["prs"] += 1
        for i in issues.values():
            if i.get("repo") == repo_name:
                for a in [_normalize_user(a) for a in i.get("assignees", [])]:
                    stats.setdefault(a, {"commits": 0, "prs": 0, "issues": 0})
                    stats[a]["issues"] += 1

        result = {"repo": repo_name, "team_stats": stats, "report_date": CURRENT_DATE}
        return _response("ok", result)
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "GetTeamContributionStats",
                "description": "Calculate contributions (commits, PRs, issues) per user deterministically.",
                "parameters": {
                    "type": "object",
                    "properties": {"repo_name": {"type": "string"}},
                    "required": ["repo_name"],
                },
            },
        }
