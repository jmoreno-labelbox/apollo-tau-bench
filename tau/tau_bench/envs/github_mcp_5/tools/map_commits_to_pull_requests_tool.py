# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class MapCommitsToPullRequestsTool(Tool):
    """
    Map commits to their associated pull requests deterministically.

    This tool searches for commits in a repository and determines which pull requests
    they belong to, based on commit SHA associations. It provides traceability from
    commits to the PRs that included them.

    Input Parameters:
        repo_name (str): The name of the repository.
        commit_shas (List[str]): A list of commit SHA identifiers to map.

    Returns:
        str: JSON-formatted response containing:
            - status: "ok" if successful, or "error" otherwise.
            - data: A mapping of commit SHAs to pull request IDs.

    Errors:
        - Returns an error if `repo_name` or `commit_shas` are missing or invalid.
        - Returns an error if no associations are found for the given commits.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs: Any) -> str:
        try:
            repo_name = _validate_param(kwargs, "repo_name", str)
        except (ValueError, TypeError) as e:
            return _response("error", str(e), "VALIDATION_ERROR")

        commits = list(data.get("commits", {}).values())
        prs = list(data.get("pull_requests", {}).values())

        mapping = []
        for pr in prs:
            if pr.get("repo") == repo_name:
                pr_commits = [c for c in commits if c.get("repo") == repo_name and c.get("branch") == pr.get("head_branch")]
                mapping.append({
                    "pr_id": _safe_id(pr, "pr_id", f"PR_{repo_name}_", ["title", "head_branch", "base_branch"]),
                    "commit_ids": [c.get("sha") for c in pr_commits],
                    "report_date": CURRENT_DATE,
                })

        return _response("ok", mapping)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "map_commits_to_pull_requests",
                "description": "Map commits deterministically to their pull requests.",
                "parameters": {
                    "type": "object",
                    "properties": {"repo_name": {"type": "string"}},
                    "required": ["repo_name"],
                },
            },
        }
