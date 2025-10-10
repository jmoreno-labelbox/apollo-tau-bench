# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class MarkPRasMerged(Tool):
    """
    Marks a pull request as merged, but only if it is currently mergeable.
    NOTE: This tool does NOT copy files or perform any branch/content merge. It only:
      - verifies the PR is mergeable,
      - sets merged flags/states,
      - bumps the PR's updated_ts deterministically,
      - logs a terminal message.
    Inputs: owner, repo_name, pr_number
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        owner = (kwargs.get("owner") or "").strip()
        repo_name = (kwargs.get("repo_name") or kwargs.get("reponame") or "").strip()
        pr_number_raw = kwargs.get("pr_number", kwargs.get("prnumber", None))

        if not owner or not repo_name or pr_number_raw is None:
            return json.dumps(
                {"error": "Required: owner, repo_name, pr_number."},
                indent=2
            )

        try:
            pr_number = int(pr_number_raw)
        except Exception:
            return json.dumps({"error": "pr_number must be an integer."}, indent=2)

        # Load PR DB
        pr_db = list(data.get("pull_requests", {}).values())
        if not isinstance(pr_db, list):
            return json.dumps({"error": "Invalid pull requests DB: expected a list."}, indent=2)

        # Find PR bucket for repo
        rec = next((r for r in pr_db if r.get("owner") == owner and r.get("repo_name") == repo_name), None)
        if rec is None:
            return json.dumps({"error": f"No pull requests found for '{owner}/{repo_name}'."}, indent=2)

        pr_numbers: List[int] = rec.get("pr_numbers", [])
        if pr_number not in pr_numbers:
            return json.dumps({"error": f"PR #{pr_number} not found for '{owner}/{repo_name}'."}, indent=2)
        idx = pr_numbers.index(pr_number)

        # Ensure arrays exist/padded
        rec.setdefault("pr_states", [])
        rec.setdefault("merged_flags", [])
        rec.setdefault("mergeable_flags", [])
        rec.setdefault("updated_ts", [])
        rec.setdefault("pr_status", [])

        while len(rec["pr_states"])       <= idx: rec["pr_states"].append("open")
        while len(rec["merged_flags"])    <= idx: rec["merged_flags"].append(False)
        while len(rec["mergeable_flags"]) <= idx: rec["mergeable_flags"].append(False)
        while len(rec["updated_ts"])      <= idx: rec["updated_ts"].append(None)
        while len(rec["pr_status"])       <= idx: rec["pr_status"].append("open")

        # Must be mergeable
        if not bool(rec["mergeable_flags"][idx]):
            return json.dumps(
                {
                    "error": f"PR #{pr_number} is not mergeable for '{owner}/{repo_name}'.",
                    "mergeable": False,
                    "current_state": rec["pr_states"][idx]
                },
                indent=2
            )

        # Idempotent path: already merged
        if bool(rec["merged_flags"][idx]) and rec["pr_states"][idx] == "merged":
            return json.dumps(
                {
                    "success": f"PR #{pr_number} is already merged for {owner}/{repo_name}.",
                    "repo": f"{owner}/{repo_name}",
                    "pr_number": pr_number,
                    "state": "merged",
                    "merged": True,
                    "mergeable": True,
                    "updated_ts": rec["updated_ts"][idx]
                },
                indent=2
            )

        # Mark as merged and update timestamp (no file operations)
        rec["pr_states"][idx] = "merged"
        rec["pr_status"][idx] = "merged"
        rec["merged_flags"][idx] = True

        new_updated_ts = get_current_updated_timestamp()
        rec["updated_ts"][idx] = new_updated_ts

        # Terminal log
        add_terminal_message(
            data,
            f"PR #{pr_number} merged for {owner}/{repo_name}.",
            new_updated_ts
        )

        return json.dumps(
            {
                "success": f"PR #{pr_number} merged for {owner}/{repo_name}.",
                "repo": f"{owner}/{repo_name}",
                "pr_number": pr_number,
                "state": "merged",
                "merged": True,
                "mergeable": True,
                "updated_ts": new_updated_ts
            },
            indent=2
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "mark_pr_as_merged",
                "description": "Mark a PR as merged if mergeable; sets merged flags/states and updates PR updated_ts (no file merges).",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string", "description": "Repository owner."},
                        "repo_name": {"type": "string", "description": "Repository name (alias: reponame)."},
                        "pr_number": {"type": "integer", "description": "Pull request number."}
                    },
                    "required": ["owner", "repo_name", "pr_number"]
                }
            }
        }
