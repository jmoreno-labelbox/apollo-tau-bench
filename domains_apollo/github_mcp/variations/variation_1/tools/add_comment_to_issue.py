from tau_bench.envs.tool import Tool
import json
from typing import Any

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
    def invoke(
        data: dict[str, Any],
        owner: str = None,
        repo_name: str = None,
        issue_number: str = None,
        issue_comment: str = None,
        issue_comment_user: str = None,
    ) -> str:
        owner = (owner or "").strip()
        repo_name = (repo_name or "").strip()
        # accept several aliases for the issue number
        issue_number_raw = issue_number

        issue_comment = (issue_comment or "").strip()
        issue_comment_user = (issue_comment_user or "").strip()

        if (
            not owner
            or not repo_name
            or issue_number_raw is None
            or not issue_comment
            or not issue_comment_user
        ):
            payload = {
                "error": "Required: owner, repo_name (or repo_name), issue_number, issue_comment, issue_comment_user."
            }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        # Normalize issue_number
        try:
            issue_number = int(issue_number_raw)
        except Exception:
            payload = {"error": "issue_number must be an integer."}
            out = json.dumps(payload, indent=2)
            return out

        # Load issues DB
        issues_db = data.get("issues", [])
        if not isinstance(issues_db, list):
            payload = {"error": "Invalid issues DB: expected a list at data['issues']."}
            out = json.dumps(
                payload, indent=2,
            )
            return out

        # Find repo bucket
        rec = next(
            (
                r
                for r in issues_db
                if r.get("owner") == owner and r.get("repo_name") == repo_name
            ),
            None,
        )
        if rec is None:
            payload = {"error": f"No issues found for repository '{owner}/{repo_name}'."}
            out = json.dumps(
                payload, indent=2,
            )
            return out

        issue_numbers: list[int] = rec.get("issue_numbers", [])
        if issue_number not in issue_numbers:
            payload = {
                "error": f"Issue #{issue_number} not found for '{owner}/{repo_name}'."
            }
            out = json.dumps(
                payload, indent=2,
            )
            return out

        idx = issue_numbers.index(issue_number)

        # Ensure arrays exist and are padded
        rec.setdefault("issue_comments", [])
        rec.setdefault("issue_comment_users", [])
        rec.setdefault("updated_ts", [])
        while len(rec["issue_comments"]) <= idx:
            rec["issue_comments"].append([])
        while len(rec["issue_comment_users"]) <= idx:
            rec["issue_comment_users"].append([])
        while len(rec["updated_ts"]) <= idx:
            rec["updated_ts"].append(None)

        # Ensure per-issue comment containers are lists
        if not isinstance(rec["issue_comments"][idx], list):
            rec["issue_comments"][idx] = []
        if not isinstance(rec["issue_comment_users"][idx], list):
            rec["issue_comment_users"][idx] = []

        # Append comment and user (keep indices aligned)
        rec["issue_comments"][idx].append(issue_comment)
        rec["issue_comment_users"][idx].append(issue_comment_user)
        comment_index = len(rec["issue_comments"][idx]) - 1

        # Bump updated_ts using environment helper
        new_updated_ts = get_current_updated_timestamp()
        rec["updated_ts"][idx] = new_updated_ts

        add_terminal_message(
            data,
            f"Comment added to issue #{issue_number} for {owner}/{repo_name}.",
            get_current_updated_timestamp(),
        )
        payload = {
            "success": f"Comment added to issue #{issue_number} for {owner}/{repo_name}.",
            "repo": f"{owner}/{repo_name}",
            "issue_number": issue_number,
            "comment_index": comment_index,
            "issue_comment": issue_comment,
            "issue_comment_user": issue_comment_user,
            "updated_ts": new_updated_ts,
        }
        out = json.dumps(
            payload, indent=2,
        )
        return out
    @staticmethod
    def get_info() -> dict[str, Any]:
        return {
            "type": "function",
            "function": {
                "name": "AddCommentToIssue",
                "description": "Append a comment to an issue and update the issue's updated_ts.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "owner": {"type": "string", "description": "Repository owner."},
                        "repo_name": {
                            "type": "string",
                            "description": "Repository name (alias: repo_name).",
                        },
                        "issue_number": {
                            "type": "integer",
                            "description": "Issue number.",
                        },
                        "issue_comment": {
                            "type": "string",
                            "description": "Comment text to add.",
                        },
                        "issue_comment_user": {
                            "type": "string",
                            "description": "Username adding the comment.",
                        },
                    },
                    "required": [
                        "owner",
                        "repo_name",
                        "issue_number",
                        "issue_comment",
                        "issue_comment_user",
                    ],
                },
            },
        }
