# Copyright Sierra

import json
from typing import Any, Dict, List, Optional
from tau_bench.envs.tool import Tool


class AddCommentToIssue(Tool):
    """
    Append a comment to an issue in the issues DB.
    Inputs:
      - owner (str)
      - repo_name (str)  [alias: repo_name]
      - issue_number (int) [alias: issue number, issue_no, number]
      - issue_comment (str)
      - issue_comment_user (str)
    Behavior:
      - Finds the repo bucket and issue by number.
      - Appends the comment and commenter to aligned arrays.
      - Bumps updated_ts for that issue via get_current_updated_timestamp().
    """

    @staticmethod
    def invoke(data: Dict[str, Any], **kwargs) -> str:
        owner = (kwargs.get("owner") or "").strip()
        repo_name = (kwargs.get("repo_name") or kwargs.get("repo_name") or "").strip()
        # allow multiple aliases for the issue identifier
        issue_number_raw = (
            kwargs.get("issue_number",
                kwargs.get("issue number",
                    kwargs.get("issue_no",
                        kwargs.get("number", None)
                    )
                )
            )
        )
        issue_comment = (kwargs.get("issue_comment") or "").strip()
        issue_comment_user = (kwargs.get("issue_comment_user") or "").strip()

        if not owner or not repo_name or issue_number_raw is None or not issue_comment or not issue_comment_user:
            return json.dumps(
                {"error": "Required: owner, repo_name (or repo_name), issue_number, issue_comment, issue_comment_user."},
                indent=2
            )

        # Standardize issue_number
        try:
            issue_number = int(issue_number_raw)
        except Exception:
            return json.dumps({"error": "issue_number must be an integer."}, indent=2)

        # Load the issues database.
        issues_db = list(data.get("issues", {}).values())
        if not isinstance(issues_db, list):
            return json.dumps({"error": "Invalid issues DB: expected a list at data['issues']."}, indent=2)

        # Locate repository bucket
        rec = next((r for r in issues_db if r.get("owner") == owner and r.get("repo_name") == repo_name), None)
        if rec is None:
            return json.dumps({"error": f"No issues found for repository '{owner}/{repo_name}'."}, indent=2)

        issue_numbers: List[int] = rec.get("issue_numbers", [])
        if issue_number not in issue_numbers:
            return json.dumps({"error": f"Issue # {issue_number} does not exist for '{owner}/{repo_name}'."}, indent=2)

        idx = issue_numbers.index(issue_number)

        # Verify the presence of arrays and apply padding.
        rec.setdefault("issue_comments", [])
        rec.setdefault("issue_comment_users", [])
        rec.setdefault("updated_ts", [])
        while len(rec["issue_comments"]) <= idx:
            rec["issue_comments"].append([])
        while len(rec["issue_comment_users"]) <= idx:
            rec["issue_comment_users"].append([])
        while len(rec["updated_ts"]) <= idx:
            rec["updated_ts"].append(None)

        # Verify that comment containers for each issue are implemented as lists.
        if not isinstance(rec["issue_comments"][idx], list):
            rec["issue_comments"][idx] = []
        if not isinstance(rec["issue_comment_users"][idx], list):
            rec["issue_comment_users"][idx] = []

        # Add comment and user while maintaining index alignment.
        rec["issue_comments"][idx].append(issue_comment)
        rec["issue_comment_users"][idx].append(issue_comment_user)
        comment_index = len(rec["issue_comments"][idx]) - 1

        # Update updated_ts utilizing the environment utility.
        new_updated_ts = get_current_updated_timestamp()
        rec["updated_ts"][idx] = new_updated_ts

        add_terminal_message(data, f"Comment added to issue # {issue_number} for {owner}/{repo_name}.")

        return json.dumps(
            {
                "success": f"Comment added to issue # {issue_number} for {owner}/{repo_name}.",
                "repo": f"{owner}/{repo_name}",
                "issue_number": issue_number,
                "comment_index": comment_index,
                "issue_comment": issue_comment,
                "issue_comment_user": issue_comment_user,
                "updated_ts": new_updated_ts
            },
            indent=2
        )

    @staticmethod
    def get_info() -> Dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "add_comment_to_issue",
                "description": "Append a comment to an issue and update the issue's updated_ts.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string", "description": "Repository owner."},
                        "repo_name": {"type": "string", "description": "Repository name (alias: repo_name)."},
                        "issue_number": {"type": "integer", "description": "Issue number."},
                        "issue_comment": {"type": "string", "description": "Comment text to add."},
                        "issue_comment_user": {"type": "string", "description": "Username adding the comment."}
                    },
                    "required": ["owner", "repo_name", "issue_number", "issue_comment", "issue_comment_user"]
                }
            }
        }