# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class GetPRDetails(Tool):
    """
    Returns all details for a pull request identified by (owner, repo_name, pr_number).
    - Accepts 'pr_number' (preferred) or 'prnumber' as an alias.
    - Reads from list(data.get('pull_requests', {}).values()) or top-level list.
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        owner = kwargs.get("owner", "").strip()
        repo_name = (kwargs.get("repo_name") or kwargs.get("repo_name") or "").strip()
        # Support both 'pr_number' and 'prnumber'
        pr_number_raw = kwargs.get("pr_number", kwargs.get("prnumber", None))

        if not owner or not repo_name or pr_number_raw is None:
            return json.dumps(
                {"error": "Parameters 'owner', 'repo_name', and 'pr_number' are required."},
                indent=2
            )

        # Normalize pr_number to int
        try:
            pr_number = int(pr_number_raw)
        except Exception:
            return json.dumps(
                {"error": "pr_number must be an integer."},
                indent=2
            )

        # Load PR DB (supports dict with 'pull_requests' or a top-level list)
        pr_db = list(data.get("pull_requests", {}).values())


        if not isinstance(pr_db, list):
            return json.dumps(
                {"error": "Invalid pull requests DB: expected a list."},
                indent=2
            )

        # Find the repo bucket
        rec = next((r for r in pr_db if r.get("owner") == owner and r.get("repo_name") == repo_name), None)
        if rec is None:
            return json.dumps(
                {"error": f"No pull requests found for repository '{owner}/{repo_name}'."},
                indent=2
            )

        pr_numbers: List[int] = rec.get("pr_numbers", [])
        if pr_number not in pr_numbers:
            return json.dumps(
                {"error": f"PR #{pr_number} not found for '{owner}/{repo_name}'."},
                indent=2
            )

        idx = pr_numbers.index(pr_number)

        # Helper to safely fetch an indexed value from a list, else None
        def _get_at(lst_name: str):
            lst = rec.get(lst_name, [])
            return lst[idx] if idx < len(lst) else None

        # Extract all relevant fields (defensive on lengths)
        details = {
            "number": pr_number,
            "title": _get_at("pr_titles"),
            "body": _get_at("pr_bodies"),
            "state": _get_at("pr_states"),
            "base_branch": _get_at("base_branches"),
            "head_branch": _get_at("head_branches"),
            "head_sha": _get_at("head_shas"),
            "mergeable": _get_at("mergeable_flags"),
            "merged": _get_at("merged_flags"),
            # Files/comments/reviews are often nested; return as stored in DB
            "files": _get_at("pr_files"),
            "comments": _get_at("pr_comments"),
            "comment_users": _get_at("pr_comment_users"),
            "reviewers": _get_at("reviewers"),
            "review_states": _get_at("review_states"),
            "review_events": _get_at("review_events"),
            "created_ts": _get_at("created_ts"),
            "updated_ts": _get_at("updated_ts"),
        }

        return json.dumps(details, indent=2)

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "get_pr_details",
                "description": "Fetch all stored details for a pull request (owner, repo_name, pr_number).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string", "description": "Repository owner."},
                        "repo_name": {"type": "string", "description": "Repository name."},
                        "pr_number": {"type": "integer", "description": "Pull request number."}
                    },
                    "required": ["owner", "repo_name", "pr_number"]
                }
            }
        }
