# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetPullRequestMergeTimeReportTool(Tool):
    """
    Generate a deterministic report of pull request merge times.

    This tool calculates how long pull requests remained open before being merged,
    by comparing their `created_at` and `updated_at` timestamps.
    Results provide insights into repository efficiency for reviewing and merging PRs.

    Input Parameters:
        repo_name (str): The name of the repository.

    Returns:
        str: JSON-formatted response containing:
            - status: "ok" if successful.
            - data: A list of merged pull requests with:
                - pr_id (str): Deterministic pull request ID.
                - title (str): The pull request title.
                - created_at (str): The PR creation timestamp.
                - merged_at (str): The PR merge timestamp.
                - merge_duration_days (int): Number of days between creation and merge.
                - report_date (str): Deterministic date stamp (CURRENT_DATE).

    Errors:
        - Returns an error if `repo_name` is missing or invalid.
        - Returns an error if no merged pull requests are found in the repository.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs: Any) -> str:
        try:
            repo_name = _validate_param(kwargs, "repo_name", str)
        except (ValueError, TypeError) as e:
            return _response("error", str(e), "VALIDATION_ERROR")

        prs = list(data.get("pull_requests", {}).values())
        merged_prs = [p for p in prs if p.get("repo") == repo_name and p.get("state") == "merged"]

        merge_times = []
        for pr in merged_prs:
            created = pr.get("created_at")
            merged = pr.get("merged_at")
            if created and merged:
                merge_times.append(_days_between(created, merged))

        average_merge_time = int(sum(merge_times) / len(merge_times)) if merge_times else 0

        report = {
            "repo": repo_name,
            "merged_pr_count": len(merged_prs),
            "average_merge_time": average_merge_time,
            "report_date": CURRENT_DATE,
        }

        return _response("ok", report)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_pull_request_merge_time_report",
                "description": "Calculate deterministic average time-to-merge for pull requests.",
                "parameters": {
                    "type": "object",
                    "properties": {"repo_name": {"type": "string"}},
                    "required": ["repo_name"],
                },
            },
        }
